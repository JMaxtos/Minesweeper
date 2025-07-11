import pygame
import pyautogui
import pygetwindow as gw
import random
import os
import time

from constants import *
from tile import *
from board import *


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        os.environ['SDL_VIDEO_CENTERED'] = '1'  # Center the Window

        # Get Pygame Window
        window = gw.getWindowsWithTitle(TITLE)[0]
        window.activate()
        win_left = window.left
        win_top = window.top

     
        # Move the mouse 
        for _ in range(6):
             
            x = random.randint(0, WIDTH - 1)
            y = random.randint(0, HEIGHT - 1)
            abs_x = win_left + x
            abs_y = win_top + y
            pyautogui.moveTo(abs_x, abs_y, duration=0.5)
            pyautogui.click(interval=0.5)


    def new(self):
        self.board = Board()
        self.board.display_board()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
        else:
            self.endScreen()

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.board.draw(self.screen)
        pygame.display.flip()

    def checkWin(self):
        for row in self.board.boardList:
            for tile in row:
                if tile.type != "M" and not tile.revealed:
                    return False
        return True

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.leaveGame()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                mx //= TILESIZE
                my //= TILESIZE

                if event.button == 1:
                    if not self.board.boardList[mx][my].flagged:
                        if not self.board.dig(mx, my):
                            for row in self.board.boardList:
                                for tile in row:
                                    if tile.flagged and tile.type != "M":
                                        tile.flagged = False
                                        tile.revealed = True
                                        tile.image = tile_NotMine
                                    elif tile.type == "M":
                                        tile.revealed = True
                                        
                            self.playing = False

                if event.button == 3:
                    if not self.board.boardList[mx][my].revealed:
                        self.board.boardList[mx][my].flagged = not self.board.boardList[mx][my].flagged

                if self.checkWin():
                    self.win = True
                    print("Congratulations you win!!!")
                    self.playing = False
                    for row in self.board.boardList:
                        for tile in row:
                            if not tile.revealed:
                                tile.flagged = True
    def endScreen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                       self.leaveGame()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    return
    def revealAllBoard(self):
         for row in self.board.boardList:
            for tile in row:
                if tile.type == "M":
                    tile.flagged = True
    
    def leaveGame(self):
        pygame.quit()
        quit(0)
        
        
        
game = Game()
while True:
    game.new()
    game.run()

