class Tile:
    def __init__(self,n,e,s,w) -> None:
        self.n = n
        self.e = e
        self.s = s
        self.w = w

    def __str__(self) -> str:
        return f"N: {self.n}, E: {self.e}, S: {self.s}, W: {self.w}"