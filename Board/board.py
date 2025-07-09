import pygame
import random
from constants import *
from tile import *
from setupTiles import *

class Board:
    def __init__(self):
        self.boardGame = pygame.Surface((WIDTH, HEIGHT))
        self.boardList = [[Tile(col, row, tile_Empty, "?") for row in range(ROWS)] for col in range(COLUMNS)]
        self.placeMines()
        self.placeClues()
        self.dug = []

    def placeMines(self):
        for _ in range(NUM_MINES):
            while True:
                x = random.randint(0, ROWS-1)
                y = random.randint(0, COLUMNS-1)

                if self.boardList[x][y].type == "?":
                    self.boardList[x][y].image = tile_Mine
                    self.boardList[x][y].type = "M"
                    break

    def placeClues(self):
        for x in range(ROWS):
            for y in range(COLUMNS):
                if self.boardList[x][y].type != "M":
                    total_mines = self.check_neighbours(x, y)
                    if total_mines > 0:
                        self.boardList[x][y].image = tile_numbers[total_mines-1]
                        self.boardList[x][y].type = "C"


    @staticmethod
    def is_inside(x, y):
        return 0 <= x < ROWS and 0 <= y < COLUMNS

    def check_neighbours(self, x, y):
        total_mines = 0
        for x_offset in range(-1, 2):
            for y_offset in range(-1, 2):
                neighbour_x = x + x_offset
                neighbour_y = y + y_offset
                if self.is_inside(neighbour_x, neighbour_y) and self.boardList[neighbour_x][neighbour_y].type == "M":
                    total_mines += 1

        return total_mines

    def draw(self, screen):
        for row in self.boardList:
            for tile in row:
                tile.draw(self.boardGame)
        screen.blit(self.boardGame, (0, 0))

    def dig(self, x, y):
        self.dug.append((x, y))
        if self.boardList[x][y].type == "M":
            self.boardList[x][y].revealed = True
            self.boardList[x][y].image = tile_Exploded
            return False
        elif self.boardList[x][y].type == "C":
            self.boardList[x][y].revealed = True
            return True

        self.boardList[x][y].revealed = True

        for row in range(max(0, x-1), min(ROWS-1, x+1) + 1):
            for col in range(max(0, y-1), min(COLUMNS-1, y+1) + 1):
                if (row, col) not in self.dug:
                    self.dig(row, col)
        return True

    def display_board(self):
        for row in self.boardList:
            print(row)