from src.Grid import Grid
from src.Player import Player

class TileTraveller:
    def __init__(self) -> None:
        self.score = 0
        self.player = Player()
        self.grid = Grid()

    def play(self):
        dir = input("Choose Direction: ")
        if dir == "w":
            self.player.move("w")
        elif dir == "e":
            self.player.move("e")

    def print_grid(self):
        print(self.grid)