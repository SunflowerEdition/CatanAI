from Board import Board

class Game:
    def __init__(self):
        self.board = Board()

    def reset(self):
        self.board.reset()