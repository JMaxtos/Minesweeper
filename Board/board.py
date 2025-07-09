import pygame
import random
from constants import *
from tile import *
from setupTiles import *

class Board:
    def __init__(self):
        self.boardGame = pygame.Surface((WIDTH,HEIGHT))
        self.boardList = [[Tile(col,row,tile_empty,"?")for row in range(ROWS)]for col in range(COLUMNS)]
        self.placeMines()
        self.placeClues()
        self.dug = []

    def draw(self, screen):
        for row in self.boardList:
            for tile in row:
                tile.draw(self.boardGame)
        screen.blit(self.boardGame, (0, 0))

    def placeMines(self):
        for i in range(NUN_MINES):
            while True:
                x = random.randint(0,ROWS-1)
                y = random.randint(0,COLUMNS-1)

                if self.boardList[x][y] == '?':
                    self.boardList[x][y].image =tile_mine
                    self.boardList[x][y].type = 'M'
                    break
    def placeClues(self):
        for x in range(ROWS):
            for y in range(COLUMNS):
                if self.boardList[x][y].type != 'M':
                    totalmines = self.checkNeighbours(x,y)
                    if totalmines > 0:
                        self.boardList[x][y].image = tile_numbers[totalmines-1]
                        self.boardList[x][y].type = 'C'

    def isInsideTheBoard(x,y):
        return 0 <= x < ROWS and 0 <= y < COLUMNS
    
    def checkNeighbours(self,x,y):
        totalMines = 0
        for i in range(-1,2):
            for j in range(-1,2):
                neighbourX = x + i
                neighbourY = y + j
                
                if self.isInsideTheBoard(neighbourX,neighbourY) and self.boardList[neighbourX][neighbourY].type == 'M':
                    totalMines +=1 
        return totalMines
    
    def draw(self,screen):
        for row in self.boardList:
            for tile in row:
                tile.draw(self.boardGame)
        screen.blit(self.boardGame,(0,0))
        
    def dig(self,x,y):
        self.dug.append((x,y))
        if self.boardList[x][y].type == 'X':
            self.boardList[x][y].revealed = True
            self.boardList[x][y].image = tile_exploded
            return False
        elif self.boardList[x][y].type == 'C':
            self.boardList[x][y].revealed = True
            return True
        
        self.boardList[x][y].revealed = True        
            
            
    def displayBoard(self):
        for row in self.boardList:
            print(row)
