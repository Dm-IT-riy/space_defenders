class Stats():

    def __init__(self, player):
        self.reset_stats()
        self.run_game = True
        self.player_name = player

    def reset_stats(self):
        """stats into game"""
        self.guns_left = 1
        self.score = 0
