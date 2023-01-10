from src.Tile import Tile

class Grid:
    def __init__(self) -> None:
        self.height = 1
        self.width = 3
        self.tiles = [[Tile(0,1,0,0),Tile(0,1,0,1),Tile(0,0,0,1)]]

    def __str__(self) -> str:
        return "".join(str(self.tiles))