import random

class Player:
    def __init__(self, index):
        """

        :param index:
        """
        self.index = index

        # Initialize the player's resources
        self.num_wool = 0
        self.num_brick = 0
        self.num_lumber = 0
        self.num_ore = 0
        self.num_grain = 0


    def reset(self):
        """
        Reset the player for a new game.

        :return:
        """
        self.num_wool = 0
        self.num_brick = 0
        self.num_lumber = 0
        self.num_ore = 0
        self.num_grain = 0


    @staticmethod
    def get_starting_position(board):
        """
        Gets the starting settlement and road.
        NOTE: FOR THE MOMENT, THIS SIMPLY SELECTS RANDOMLY

        :param board: The game board
        :return: (Settlement index, Road index) tuple
        """
        # Get all legal nodes and select one randomly
        node = random.choice(board.get_all_legal_nodes())

        # Get all legal edges from that node and select one randomly
        edge = random.choice(node.get_unowned_edges())

        return node.index, edge.index
