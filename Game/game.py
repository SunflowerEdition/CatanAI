from board import Board
from player import Player
from topology import create_four_player_board

class Game:
    def __init__(self):
        self.board = create_four_player_board()
        self.players = [Player(index) for index in range(4)]

    def reset(self):
        """
        Reset the game by resetting the board and the players.

        :return: None
        """
        self.board.reset()
        for player in self.players:
            player.reset()

    def run_starting_positions(self):
        """
        Gets the starting settlements and roads for each player
        and applies them to the board.

        :return: None
        """
        # Get their first settlement and road
        for player in self.players:
            settlement_idx, road_idx = player.get_starting_position(self.board)

        # Get their second settlement and road
        for player in reversed(self.players):
            settlement_idx, road_idx = player.get_starting_position(self.board)