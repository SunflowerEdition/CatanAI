import pygame
from constants import TileType

class Renderer:
    def __init__(self, game, window_size=(1500, 900), image_scale=0.15):
        """
        The renderer that renders the game.

        :param game: The game object that stores all the game logic
        :param window_size: The size of the render window
        :param image_scale: The amount to scale the image by
        """
        self.game = game
        self.window_width, self.window_height = window_size
        self.image_scale = image_scale

        # Initialize Pygame
        pygame.init()

        # Create the screen
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Catan")

        # Surfaces for layering
        self.static_surface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.dynamic_surface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)

        # Load images
        self.hex_width, self.hex_height, self.hex_images = self._load_hex_images()
        self.water_image = self._load_water_image()

        # Manually measured and scaled to get hex starting points
        self.hex_start_y = 550 * self.image_scale
        self.hex_start_x = 1720 * self.image_scale
        self.hex_padding_x = 10 * self.image_scale
        self.hex_padding_y = 10 * self.image_scale

        # Initialize storage for storing tile, node, and edge positions on the board
        self.tile_positions = []
        self.node_positions = []
        self.edge_positions = []

        # Used for determining edge positions and sizing
        self.edge_width_frac = 0.4
        self.edge_position_shift = [ # how much to shift the edge over (times edge width)
            (0.25, 0.125), (0.75, 0.125), (0, 0.5),
            (1.0, 0.5), (0.25, 0.875), (0.75, 0.875)
        ]
        self.edge_angle_shift = [30, -30, 90, 90, -30, 30] # how many degrees to rotate the edge

        # Used for determining node positions and sizing
        self.node_width_frac = 0.5
        self.node_position_shift = [ # how much to shift the node over (times edge width)
            (0, 0.25), (0.5, 0), (1.0, 0.25),
            (0, 0.75), (0.5, 1.0), (1.0, 0.75)
        ]

        # Used to get the color based on the player's index
        self.player_colour = [(255, 0, 0), (0, 0, 255), (255, 255, 255), (255, 165, 0)]


    def reset(self):
        # Reset tile positions
        self.tile_positions = []
        self.node_positions = []
        self.edge_positions = []

        # Clear both layers
        self.static_surface.fill((0, 0, 0, 0))
        self.dynamic_surface.fill((0, 0, 0, 0))

        # Build static layer
        self._draw_static_layer()


    def render(self):
        self._draw_dynamic_layer()
        self.screen.blit(self.static_surface, (0, 0))
        self.screen.blit(self.dynamic_surface, (0, 0))
        pygame.display.flip()


    @staticmethod
    def close():
        """
        Close the environment and clean up resources.
        """
        pygame.quit()


    def _load_hex_images(self):
        """
        Loads and scales all hex images.

        :return: hex width, hex height, and all scaled images stored in a dict
        """
        # Initialize image dict (indexed using TileType)
        images = {}

        # Create hex paths
        path = "./Assets/Hexes/"
        hex_types = [
            (TileType.DESERT, path + "desert.png"),
            (TileType.FIELD, path + "field.png"),
            (TileType.FOREST, path + "forest.png"),
            (TileType.HILL, path + "hill.png"),
            (TileType.MOUNTAIN, path + "mountain.png"),
            (TileType.PASTURE, path + "pasture.png")
        ]

        # Get hex height and width from image
        img = pygame.image.load(path + "desert.png").convert_alpha()
        src_width, src_height = img.get_size()

        # Scale hex height and width down
        hex_width = self.image_scale * src_width
        hex_height = self.image_scale * src_height

        # Scale all images based on width and height
        for tile_type, filename in hex_types:
            img = pygame.image.load(filename).convert_alpha()
            img = pygame.transform.scale(img, (hex_width, hex_height))
            images[tile_type] = img

        return hex_width, hex_height, images


    def _load_water_image(self):
        """
        Loads and scales the outline of the board

        :return: The single image of the outline
        """
        img = pygame.image.load("./Assets/Water/water-full.png").convert_alpha()
        src_width, src_height = img.get_size()
        img = pygame.transform.scale(img, (src_width * self.image_scale, src_height * self.image_scale))
        return img


    def _draw_static_layer(self):
        # Draw background for the board
        self.static_surface.fill((239, 218, 139))

        # Place water tiles
        water_width, water_height = self.water_image.get_size()
        centered_width = (self.window_width - water_width) / 2
        centered_height = (self.window_height - water_height) / 2
        rect = self.water_image.get_rect(topleft=(centered_width, centered_height))
        self.static_surface.blit(self.water_image, rect)

        # Place the land hexes and store their positions
        hex_x = self.hex_start_x + centered_width
        hex_y = self.hex_start_y + centered_height
        for i, tile in enumerate(self.game.board.tiles):
            img = self.hex_images[tile.resource_type]
            rect = img.get_rect(topleft=(hex_x, hex_y))
            self.static_surface.blit(img, rect)
            self.tile_positions.append((hex_x, hex_y))

            if i == 2 or i == 11:
                hex_x = self.hex_start_x - self.hex_width / 2  + centered_width
                hex_y += 0.75 * self.hex_height + self.hex_padding_y
            elif i == 6:
                hex_x = self.hex_start_x - self.hex_width  + centered_width
                hex_y += 0.75 * self.hex_height + self.hex_padding_y
            elif i == 15:
                hex_x = self.hex_start_x  + centered_width
                hex_y += 0.75 * self.hex_height + self.hex_padding_y
            else:
                hex_x += self.hex_width + self.hex_padding_x

    def _draw_dynamic_layer(self):
        # Reset the dynamic layer
        self.dynamic_surface.fill((0, 0, 0, 0))

        # So edges and nodes on multiple tiles don't get drawn multiple times
        added_edge_indices = []
        added_node_indices = []

        # For each hex, check what needs to be drawn
        for i, tile in enumerate(self.game.board.tiles):
            tile_x, tile_y = self.tile_positions[i]
            tile_w, tile_h = self.hex_width, self.hex_height

            # Check edges
            for j, edge in enumerate(tile.edges):
                if edge.owned_by is not None and edge.index not in added_edge_indices: # Needs to be drawn
                    # Add it so it doesn't get drawn twice
                    added_edge_indices.append(edge.index)

                    # Get its position and angle shift
                    shift_frac_x, shift_frac_y = self.edge_position_shift[j]
                    angle = self.edge_angle_shift[j]

                    # Compute the position of the edge rectangle
                    pos_x = tile_x + tile_w * shift_frac_x
                    pos_y = tile_y + tile_h * shift_frac_y

                    # Compute the size of the edge
                    edge_w = self.edge_width_frac * tile_w
                    edge_h = self.edge_width_frac * 20

                    # Create a surface for the edge
                    edge_surf = pygame.Surface((edge_w, edge_h), pygame.SRCALPHA)
                    edge_surf.fill(self.player_colour[edge.owned_by.index])

                    # Rotate the surface
                    edge_surf = pygame.transform.rotate(edge_surf, angle)

                    # Because rotation changes size, recenter
                    rect = edge_surf.get_rect(center=(pos_x, pos_y))

                    # Draw the edge
                    self.dynamic_surface.blit(edge_surf, rect)

            # Check nodes
            for j, node in enumerate(tile.nodes):
                if node.owned_by is not None and node.index not in added_node_indices: # Needs to be drawn
                    # Add it so it doesn't get drawn twice
                    added_node_indices.append(node.index)

                    # Get its position shift
                    shift_frac_x, shift_frac_y = self.node_position_shift[j]

                    # Compute the position of the node
                    pos_x = tile_x + tile_w * shift_frac_x
                    pos_y = tile_y + tile_h * shift_frac_y

                    # Compute the radius of the node
                    radius = self.node_width_frac * 20

                    # Create a surface for the edge
                    if node.city:
                        # Square for city, centered on the node
                        rect = pygame.Rect(0, 0, 2*radius, 2*radius)
                        rect.center = (pos_x, pos_y)
                        pygame.draw.rect(self.dynamic_surface, self.player_colour[node.owned_by.index], rect)
                    else:
                        # Circle for settlement
                        pygame.draw.circle(self.dynamic_surface, self.player_colour[node.owned_by.index], (int(pos_x), int(pos_y)), int(radius))


    # --- Functions used for testing --- #
    def testing_tiles(self):
        # Get font
        font = pygame.font.Font(None, 32)

        # Draw the tile indices
        for index, (x, y) in enumerate(self.tile_positions):
            tile_index = self.game.board.tiles[index].index
            text = font.render(str(tile_index), True, (255, 255, 0))
            self.static_surface.blit(text, (x + 50, y + 50))
            self.render()

            print(f"TILE INDEX: {index} -> TILE TYPE: {self.game.board.tiles[index].resource_type.name}")
