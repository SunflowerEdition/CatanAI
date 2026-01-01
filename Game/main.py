from game import Game
from renderer import Renderer

if __name__ == "__main__":
    game = Game()
    render = Renderer(game)

    while True:
        game.reset()
        render.reset()
        render.render()
        input("Waiting")
