from Board.tile import Tile

class AI_Tile(Tile):
    def __init__(self,x,y,image=None, type="?",revealed=False,flagged=False):
        super().__init__(x,y,image,type,revealed,flagged)
        self.value = 0
    
    def gameState(self):
        if self.revealed:
            if self.type == "M":
                return 9 #Mine revealed
            elif self.type == "C":
                return self.value #Clue number
            else:
                return 0 #Empty tile
        elif self.flagged:
            return -2 #Flagged tile
        else:
            return -1 #Unknown tile