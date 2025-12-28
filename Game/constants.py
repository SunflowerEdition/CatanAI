from enum import Enum

class TileType(Enum):
    FOREST = 0
    HILLS = 1
    PASTURE = 2
    FIELDS = 3
    MOUNTAINS = 4
    DESERT = 5

TILE_DISTRIBUTION = {
    TileType.FOREST: 4,
    TileType.HILLS: 3,
    TileType.PASTURE: 4,
    TileType.FIELDS: 4,
    TileType.MOUNTAINS: 3,
    TileType.DESERT: 1
}

NUM_TILES = 19
NUM_NODES = 54