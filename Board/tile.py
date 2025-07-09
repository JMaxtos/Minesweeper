from constants import TILESIZE
from setupTiles import *
class Tile:
    # "?" -> unknown
    # "M" -> mine
    # "C" -> clue
    # "/" ->empty
    def __init__(self,x,y,image,type,revealed='False',flagged='False'):
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.image = image
        self.type = type
        self.revealed = revealed
        self.flagged = flagged
    
    def draw(self, boardGame):
        if not self.flagged and self.revealed:
            boardGame.blit(self.image,(self.x,self.y))  
        elif self.flagged and not self.revealed:
            boardGame.blit(tile_flag,(self.x,self.y))
        else: 
            boardGame.blit(tile_Unknown,(self.x,self.y))

    def __repr__(self):
        return self.type