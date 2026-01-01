import pygame
from constants import TileType

class Renderer:
    def __init__(self, game, window_size=(1500, 900), image_scale=0.15):
        """
        The renderer that renders the game.

        :param game: The game object that stores all the game logic
        :param window_size: The size of the render window
        :param target_hex_width: The target hex width
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


    def reset(self):
        # Clear both layers
        self.static_surface.fill((0, 0, 0, 0))
        self.dynamic_surface.fill((0, 0, 0, 0))

        # Build static layer
        self._draw_static_layer()


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

        # Place the land hexes
        hex_x = self.hex_start_x + centered_width
        hex_y = self.hex_start_y + centered_height
        for i, tile in enumerate(self.game.board.tiles):
            img = self.hex_images[tile.resource_type]
            rect = img.get_rect(topleft=(hex_x, hex_y))
            self.static_surface.blit(img, rect)

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


    def render(self):
        self.screen.blit(self.static_surface, (0, 0))
        self.screen.blit(self.dynamic_surface, (0, 0))
        pygame.display.flip()