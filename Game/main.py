from game import Game
from renderer import Renderer

if __name__ == "__main__":
    game = Game()
    render = Renderer(game)

    # Initialize game and renderer
    game.reset()
    render.reset()
    render.render()

    # Get starting positions (THIS NEEDS TO BE IMPLEMENTED)
    game.run_starting_positions()


    # Run tests
    choice = ""
    while choice != "done":
        choice = input("Reinitialize (1) | Test Tiles (2) | ")
        if choice == "1":
            game.reset()
            render.reset()
            render.render()
        elif choice == "2":
            render.testing_tiles()
