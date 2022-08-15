import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores
import sys
from socket import *

def player():
    player = input('Enter your name: ')
    return player

def run(player = 'Dima'):
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Space defenders")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    controls.create_army(screen, aliens)
    stats = Stats(player)
    sc = Scores(screen, stats)

    while True:
        status = controls.events(screen, gun, bullets, stats)
        if status != None and status[0] == -1:
            client(scores = status[1], player = player)
            sys.exit()
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, sc, gun, aliens, bullets)
            controls.update_bullets(screen, stats, sc, aliens, bullets)
            status = controls.update_aliens(stats, screen, sc, gun, aliens, bullets)
            if status != None:
                client(scores = status, player = player)
                sys.exit()            

def client(scores, player):
    info = player, scores

    client = socket(
        AF_INET, SOCK_STREAM
    )

    client.connect(
        ('***', 7000)
    )

    data = client.recv(1024)
    message = data.decode('utf-8')
    print(f'Server message: {message}')

    client.send(f"{info}".encode('utf-8'))    

def main():
    run(player())

if __name__ == '__main__':
    main()