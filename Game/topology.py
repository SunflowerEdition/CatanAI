from Board import Board
from tile import Tile
from node import Node
from edge import Edge

def create_four_player_board():
    """
    Creates the tiles, nodes, edges, and ports for a board for four players.
    Creates all the relationships between the elements as well. View Figure 1
    for the indexing of each tile, node, edge, and port.

    :return: The Board object containing all the initialized elements
    """
    # Board constants
    NUM_TILES = 19
    NUM_EDGES = 72
    NUM_NODES = 54
    NUM_PORTS = 9

    # Declare which tiles each node falls under
    tile_nodes = [
        [0, 1, 2, 8, 9, 10], # Tile 0
        [2, 3, 4, 10, 11, 12], # Tile 1
        [4, 5, 6, 12, 13, 14], # Tile 2
        [7, 8, 9, 17, 18, 19], # Tile 3
        [9, 10, 11, 19, 20, 21], # Tile 4
        [11, 12, 13, 21, 22, 23], # Tile 5
        [13, 14, 15, 23, 24, 25], # Tile 6
        [16, 17, 18, 27, 28, 29], # Tile 7
        [18, 19, 20, 20, 30, 31], # Tile 8
        [20, 21, 22, 31, 32, 33], # Tile 9
        [22, 23, 24, 33, 34, 35], # Tile 10
        [24, 25, 26, 35, 36, 37], # Tile 11
        [28, 29, 30, 38, 39, 40], # Tile 12
        [30, 31, 32, 40, 41, 42], # Tile 13
        [32, 33, 34, 42, 43, 44], # Tile 14
        [34, 35, 36, 44, 45, 46], # Tile 15
        [39, 40, 41, 47, 48, 49], # Tile 16
        [41, 42, 43, 49, 50, 51], # Tile 17
        [43, 44, 45, 51, 52, 53] # Tile 18
    ]

    # Declare which tiles each edge falls under
    tile_edges = [
        [0, 1, 6, 7, 11, 12], # Tile 0
        [2, 3, 7, 8, 13, 14], # Tile 1
        [4, 5, 8, 9, 15, 16], # Tile 2
        [10, 11, 18, 19, 24, 25], # Tile 3
        [12, 13, 19, 20, 26, 27], # Tile 4
        [14, 15, 20, 21, 28, 29], # Tile 5
        [16, 17, 21, 22, 30, 31], # Tile 6
        [23, 24, 33, 34, 39, 40], # Tile 7
        [25, 26, 34, 35, 41, 42], # Tile 8
        [27, 28, 35, 36, 43, 44], # Tile 9
        [29, 30, 36, 37, 45, 46], # Tile 10
        [31, 32, 37, 38, 47, 48], # Tile 11
        [40, 41, 49, 50, 54, 55], # Tile 12
        [42, 43, 50, 51, 56, 57], # Tile 13
        [44, 45, 51, 52, 58, 59], # Tile 14
        [46, 47, 52, 53, 60, 61], # Tile 15
        [55, 56, 62, 63, 66, 67], # Tile 16
        [57, 58, 63, 64, 68, 69], # Tile 17
        [59, 60, 64, 65, 70, 71] # Tile 18
    ]

    # Declare which nodes are ports
    node_ports = {
        0: 0,
        1: 0,
        3: 1,
        4: 1,
        14: 2,
        15: 2,
        26: 3,
        37: 3,
        45: 4,
        46: 4,
        50: 5,
        51: 5,
        47: 6,
        48: 6,
        28: 7,
        38: 7,
        7: 8,
        17: 8
    }

    # Declare which edges belong to which nodes
    node_edges = [
        [0, 6], # Node 0
        [0, 1], # Node 1
        [1, 2, 7], # Node 2
        [2, 3], # Node 3
        [3, 4, 8], # Node 4
        [4, 5], # Node 5
        [5, 9], # Node 6
        [10, 18], # Node 7
        [10, 11], # Node 8
        [11, 12, 19], # Node 9
        [7, 12, 13], # Node 10
        [13, 14, 29], # Node 11
        [8, 14, 15], # Node 12
        [15, 16, 21], # Node 13
        [9, 16, 17], # Node 14
        [17, 22], # Node 15
        [23, 33], # Node 16
        [18, 23, 24], # Node 17
        [24, 25, 34], # Node 18
        [19, 25, 26], # Node 19
        [26, 27, 35], # Node 20
        [20, 27, 28], # Node 21
        [28, 29, 36], # Node 22
        [21, 29, 30], # Node 23
        [], # Node 24
        [], # Node 25
        [], # Node 26
        [], # Node 27
        [], # Node 28
        [], # Node 29
        [], # Node 30
        [], # Node 31
        [], # Node 32
        [], # Node 33
        [], # Node 34
        [], # Node 35
        [], # Node 36
        [], # Node 37
        [], # Node 38
        [], # Node 39
        [], # Node 40
        [], # Node 41
        [], # Node 42
        [], # Node 43
        [], # Node 44
        [], # Node 45
        [], # Node 46
        [], # Node 47
        [], # Node 48
        [], # Node 49
        [], # Node 50
        [], # Node 51
        [], # Node 52
        []  # Node 53
    ]


    # Create Edge objects
    edges = [Edge() for _ in range(NUM_EDGES)]

    # Create Node objects
    nodes = []



    # Create the board object
    board = Board(num_tiles=NUM_TILES, num_edges=NUM_EDGES, num_nodes=NUM_NODES, num_ports=NUM_PORTS)

    # Extract tiles, nodes, and edges for easy manipulation
    tiles = board.tiles
    nodes = board.nodes
    edges = board.edges

    # Add relationships
    for tile_index in range(NUM_TILES):
        for node_index in tile_nodes[tile_index]:
            tiles[tile_index].nodes.append(nodes[node_index])

        for edge_index in tile_edges[tile_index]:
            tiles[tile_index].edges.append(edges[edge_index])
