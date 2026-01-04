from game import Game
from renderer import Renderer

if __name__ == "__main__":
    game = Game()
    render = Renderer(game)

    # Initialize game and renderer
    game.reset()
    render.reset()
    render.render()

    # Get starting positions
    game.get_starting_positions()
