import pygame
from constants import *
from tile  import *
from board import *


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        