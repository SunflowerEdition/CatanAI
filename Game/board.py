from tile import Tile
from node import Node
from edge import Edge
from constants import *

class Board:
    def __init__(self):
        tiles = [Tile() for _ in range(NUM_TILES)]
        nodes = [Node() for _ in range(NUM_NODES)]
        edges = []

    def reset(self):
        # Shuffle resource order
