import pygame
from constants import TileType

class Renderer:
    def __init__(self, game, window_size=(1200,800), hex_size=150):
        self.game = game
        self.window_size = window_size
        self.hex_size = hex_size

        # Initialize Pygame and create the screen
        pygame.init()
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Catan")

        # Surfaces for layering
        self.static_surface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.dynamic_surface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)

        # Load images
        self.hex_images = self.load_hex_images()


    def load_hex_images(self):
        images = {}
        path = "./Assets/Hexes/"
        hex_types = [
            (TileType.DESERT, path + "desert.png"),
            (TileType.FIELD, path + "field.png"),
            (TileType.FOREST, path + "forest.png"),
            (TileType.HILL, path + "hill.png"),
            (TileType.MOUNTAIN, path + "mountain.png"),
            (TileType.PASTURE, path + "pasture.png"),
            ("WATER", path + "water.png")
        ]

        for tile_type, filename in hex_types:
            img = pygame.image.load(filename).convert_alpha()
            img = pygame.transform.scale(img, (self.hex_size, self.hex_size))
            images[tile_type] = img

        return images


    def reset(self):
        # Clear both layers
        self.static_surface.fill((0, 0, 0, 0))
        self.dynamic_surface.fill((0, 0, 0, 0))

        # Build static layer
        self._draw_static_layer()


    def _draw_static_layer(self):
        # Place the water hexes
        img = self.hex_images["WATER"]
        rect = img.get_rect(topleft=(0,0))
        self.static_surface.blit(img, rect)

        # Place the land hexes
        hex_x = 2 * self.hex_size
        hex_y = self.hex_size
        for i, tile in enumerate(self.game.board.tiles):
            img = self.hex_images[tile.resource_type]
            rect = img.get_rect(topleft=(hex_x, hex_y))
            self.static_surface.blit(img, rect)

            if i == 2 or i == 11:
                hex_x = 3 * self.hex_size / 2
                hex_y += 0.75 * self.hex_size
            elif i == 6:
                hex_x = self.hex_size
                hex_y += 0.75 * self.hex_size
            elif i == 15:
                hex_x = 2 * self.hex_size
                hex_y += 0.75 * self.hex_size
            else:
                hex_x += self.hex_size


    def render(self):
        self.screen.blit(self.static_surface, (0, 0))
        self.screen.blit(self.dynamic_surface, (0, 0))
        pygame.display.flip()