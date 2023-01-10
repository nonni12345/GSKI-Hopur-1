from src.Grid import Grid
from src.Player import Player

class TileTraveller:

    def __init__(self) -> None:

        self.score = 0
        self.player = Player()
        self.grid = Grid()

    def play(self):

        dir = input("Choose Direction: ").lower()
        if dir == "w":
            self.is_move_true(dir)
            self.player.move("w")
        elif dir == "e":
            self.is_move_true(dir)
            self.player.move("e")
        elif dir == "n":
            self.is_move_true(dir)
            self.player.move("n")
        elif dir == "s":
            self.is_move_true(dir)
            self.player.move("s")
        else:
            print("Invalid Input")


    def is_move_true(self, dir):
        pass

    def print_grid(self):
        print(self.grid.display_grid())


    def display_player(self):
        print(f"x: {self.player.x} y: {self.player.y} {self.grid.tiles[self.player.y-1][self.player.x-1]}")

