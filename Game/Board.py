from tile import Tile
import random
from constants import TileType

class Board:
    def __init__(self):
        """
        Creates the board based on the given parameters. Creates and initializes all board
        elements as well as any dependencies between them.
        """
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

        # Create tile objects
        self.tiles = [Tile() for _ in range(len(self.tile_types))]

    def reset(self):
        # Reset each tile type, setting their resource, and dice value

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
