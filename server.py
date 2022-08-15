from socket import *
import re
import telebot

bot = telebot.TeleBot('***')

server = socket(
    AF_INET, SOCK_STREAM
)

server.bind(
    ('***', 7000)
)

server.listen(2)

while True:
    user, addr = server.accept()
    print(f'Connected:\n{user}\n{addr}')

    user.send('You are connected...'.encode('utf-8'))

    message = re.split(r"\s", user.recv(1024).decode('utf-8'))
    tokens = []
    for line in message:
        line = re.findall(r'\w+|,|\'|\"', line)
        if len(line) >= 1:
            for token in line:
                tokens.append(token)

    bot.send_message('***', f'Player {tokens[1]} received {tokens[-1]} points!')
