from src.Tile import Tile

class Grid:
    def __init__(self) -> None:
        self.height = 3
        self.width = 3
        self.tiles = [
        [Tile(1,0,0,0),Tile(1,0,0,0),Tile(1,0,0,0)],
        [Tile(1,1,1,0),Tile(0,0,1,1),Tile(1,0,1,0)],
        [Tile(0,1,1,0),Tile(0,1,0,1),Tile(0,0,1,1)]
    ]

        self.build_grid()

    def display_grid(self):
        for x in self.tiles:
            for tile in x:
                print(tile, end=" - ")


    def build_grid(self):
        for h in range(self.height):
            line = []
            for w in range(self.width):
                line.append(Tile(1,1,1,1))
            self.tiles.append(line)
                