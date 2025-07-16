from Board.board import Board
from ai_tile import AI_Tile
from Board.setupTiles import *
from Board.constants import COLUMNS,ROWS


class AIBoard(Board):
    #Board class without the Pygame
    def __init__(self):
        self.boardList = [[AI_Tile(col, row, tile_Empty, "?") for row in range(ROWS)] for col in range(COLUMNS)]
        self.placeMines()
        self.placeClues()
        self.dug = []

    def placeClues(self):
        for x in range(ROWS):
            for y in range(COLUMNS):
                if self.boardList[x][y].type != "M":
                    total_mines = self.check_neighbours(x, y)
                    self.boardList[x][y].value = total_mines
                    if total_mines > 0:
                        self.boardList[x][y].type = "C"

    def dig(self,x,y):
        tile = self.boardList[x][y]

        if tile.revealed or tile.flagged:
            return True
       
        self.dug.append((x,y))

        if tile.type == "M":
            tile.revealed = True
            return False #Lost the Game
        elif tile.type == "C":
            tile.revealed = True
            return True #Continue Game
        else:
            tile.revealed = True
            #Digs the tiles until it reaches a clue

            for row in range(max(0, x-1), min(ROWS-1, x+1) + 1):
                for col in range(max(0, y-1), min(COLUMNS-1, y+1) + 1):
                    if (row, col) not in self.dug:
                        self.dig(row, col)
            return True
    
    def getGameState(self):
        return [[tile.gameState() for tile in row]for row in self.boardList]


    def checkWin(self):
        for row in self.boardList:
            for tile in row:
                if tile.type != "M" and not tile.revealed:
                    return False
        return True