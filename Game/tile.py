class Tile:
    def __init__(self, index):
        """
        Create a new tile. The tile is the hexagon as a whole, and contains
        its resource, dice value, nodes, and edges, and any related methods

        :param index: The index (id) of the tile
        """
        self.index = index
        self.resource_type = None
        self.dice_value = None

        # Nodes and edges belonging to the tile. These do not get reset after each game.
        self.nodes = []
        self.edges = []

    def reset(self, resource_type, dice_value):
        self.resource_type = resource_type
        self.dice_value = dice_value
