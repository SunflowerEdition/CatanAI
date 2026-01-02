from enum import Enum

class TileType(Enum):
    FOREST = 0
    HILL = 1
    PASTURE = 2
    FIELD = 3
    MOUNTAIN = 4
    DESERT = 5

FOUR_PLAYER_TILE_DISTRIBUTION = {
    TileType.FOREST: 4,
    TileType.HILL: 3,
    TileType.PASTURE: 4,
    TileType.FIELD: 4,
    TileType.MOUNTAIN: 3,
    TileType.DESERT: 1
}
