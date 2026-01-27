import gymnasium as gym
import numpy as np
from Game.game import Game
from Game.renderer import Renderer
from constants import TileType

class CatanEnvironment(gym.Env):
    """
    A Gymnasium environment for the game Catan
    """

    def __init__(self, render_mode=None):
        """
        Initialize the Catan environment

        :param render_mode: Rendering mode
        """
        # Internal state
        self.game = Game()

        # Initialize rendering if required
        self.render_mode = render_mode
        if self.render_mode == "human":
            self.game_visual = Renderer(self.game)

        # Game constants
        self.NUM_TILES = len(self.game.board.tiles) # Number of tiles on the board
        self.NUM_NODES = 54
        self.NUM_EDGES = 72

        # --- Observation Space --- #

        # Tile representation: Each index represents a tile on the board
        # Channels:
        #   0-5: One-hot encoding of TileType
        #   6: Number token (normalized to 0.0-1.0)
        #   7: Whether the robber is present (binary)
        self.NUM_TILE_CHANNELS = 8
        self.NUMBER_TOKEN_IDX = 6
        self.ROBBER_IDX = 7
        tile_space = gym.spaces.Box(
            low = np.zeros((self.NUM_TILES, self.NUM_TILE_CHANNELS), dtype=np.float32),
            high = np.ones((self.NUM_TILES, self.NUM_TILE_CHANNELS), dtype=np.float32),
            shape = (self.NUM_TILES, self.NUM_TILE_CHANNELS),
            dtype=np.float32
        )

        # Node representation: Each index represents a node on the board
        # Channels:
        #   0-4: Owner (One-hot: None, Me, Opponent 1, Opponent 2, Opponent 3)
        #   5-7: Type (One-hot: Empty, Settlement, City)
        self.NUM_NODE_CHANNELS = 8
        self.NONE_IDX = 0
        self.ME_IDX = 1
        self.OPP_ONE_IDX = 2
        self.OPP_TWO_IDX = 3
        self.OPP_THREE_IDX = 4
        self.EMPTY_IDX = 5
        self.SETTLEMENT_IDX = 6
        self.CITY_IDX = 7
        node_space = gym.spaces.Box(
            low=np.zeros((self.NUM_NODES, self.NUM_NODE_CHANNELS), dtype=np.float32),
            high=np.ones((self.NUM_NODES, self.NUM_NODE_CHANNELS), dtype=np.float32),
            shape=(self.NUM_NODES, self.NUM_NODE_CHANNELS),
            dtype=np.float32
        )

        # Edge representation: Each index represents an edge on the board
        # Channels:
        #   0-4: Owner (One-hot: None, Me, Opponent 1, Opponent 2, Opponent 3)
        #   Note: uses same indexing as Node Channels
        self.NUM_EDGE_CHANNELS = 4
        edge_space = gym.spaces.Box(
            low=np.zeros((self.NUM_EDGES, self.NUM_EDGE_CHANNELS), dtype=np.float32),
            high=np.ones((self.NUM_EDGES, self.NUM_EDGE_CHANNELS), dtype=np.float32),
            shape=(self.NUM_EDGES, self.NUM_EDGE_CHANNELS),
            dtype=np.float32
        )


    def _get_obs(self):
        return


    def _get_info(self):
        """
        Returns diagnostic information for debugging/monitoring.

        :return: Auxiliary information associated to the current state
        """
        return


    def reset(self, seed=None, options=None):
        """
        Reset the environment to start a new episode.

        :param seed: Random seed for reproducibility
        :param options: Additional options for environment reset
        :return: Tuple of (observation, info) for the initial state
        """
        super().reset(seed=seed)

        # Reset the game
        self.game.reset()

        # Render if required
        if self.render_mode == "human":
            self.game_visual.reset()


    def step(self, action):
        """
        Executes one timestep of the environment

        :param action:
        :return: Tuple of (observation, reward, done, truncated, info)
        """


    def render(self, delay=0.0):
        """
        Render the environment.
        """
        return


    def close(self):
        """
        Close the Pygame window and clean up resources.
        """
        if self.game_visual:
            self.game_visual.close()
            self.game_visual = None