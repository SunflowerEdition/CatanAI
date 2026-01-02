from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player() for _ in range(4)]

    def reset(self):
        self.board.reset()
        for player in self.players:
            player.reset()

    def starting_positions(self):
        