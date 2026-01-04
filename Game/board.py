from tile import Tile
import random
from constants import TileType

class Board:
    def __init__(self, tiles, nodes, edges):
        """
        Creates the board based on the given parameters.

        :param tiles: The tiles of the board.
        :param nodes: The nodes of the board.
        :param edges: The edges of the board.
        :return: None
        """
        self.tiles = tiles
        self.nodes = nodes
        self.edges = edges

        # Used for placing dice values on tiles during setup
        self.TOKEN_TILE_IDX_ORDER = [0, 3, 7, 12, 16, 17, 18, 15, 11, 6, 2, 1, 4, 8, 13, 14, 10, 5, 9]
        self.TOKEN_DICE_VALUE_ORDER = [5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11]

        # Tile distribution for a 4-player game
        TILE_DISTRIBUTION = {
            TileType.FOREST: 4,
            TileType.HILL: 3,
            TileType.PASTURE: 4,
            TileType.FIELD: 4,
            TileType.MOUNTAIN: 3,
            TileType.DESERT: 1
        }
        self.tile_types = [tile_type for tile_type, count in TILE_DISTRIBUTION.items() for _ in range(count)]


    def reset(self):
        """
        Reset the owner of each tile, node, and edge, and reshuffle
        the resource and dice value assigned to each tile.

        :return: None
        """
        # Reset the nodes and edges
        for node in self.nodes:
            node.reset()
        for edge in self.edges:
            edge.reset()

        # Shuffle resource order
        random.shuffle(self.tile_types)

        # Reset tiles
        dice_value_index = 0
        for resource_index, tile_index in enumerate(self.TOKEN_TILE_IDX_ORDER):
            # Get the resource type and dice value for the tile
            resource_type = self.tile_types[resource_index]
            dice_value = None if resource_type == TileType.DESERT else self.TOKEN_DICE_VALUE_ORDER[dice_value_index]

            # Increment dice value index only if value is used
            if dice_value is not None:
                dice_value_index += 1

            # Reset tile with updated values
            self.tiles[tile_index].reset(resource_type, dice_value)


    def get_all_legal_nodes(self):
        """
        Selects all nodes that can be legally built on. This is
        used during the build phase at the start of the game to
        determine legal settlement placements.

        :return: List of legal nodes
        """
        # All nodes start as legal
        legal_nodes_indices = [1] * len(self.nodes)

        for node in self.nodes:
            # If node is owned,
            if node.owned_by is not None:
                # The node itself is not legal
                legal_nodes_indices[node.index] = 0

                # All neighbouring nodes are illegal
                for edge in node.edges:
                    neighbouring_node = edge.get_neighbour(node)
                    legal_nodes_indices[neighbouring_node.index] = 0

        # Create and return list of nodes from the indices
        return [self.nodes[i] for i in  legal_nodes_indices]
