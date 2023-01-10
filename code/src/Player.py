class Player:
    def __init__(self) -> None:
        self.x = 1
        self.y = 2
    
    def move(self,dir):
        if dir == "e":
            self.x += 1
        elif dir == "w":
            self.x -= 1
        
