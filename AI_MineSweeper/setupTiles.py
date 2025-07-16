import pygame
import os
from constants import TILESIZE

tile_numbers = []

# Carrega as tiles numeradas (Tile1.png até Tile8.png)
for num in range(1, 9):
    image = pygame.transform.scale(
        pygame.image.load(os.path.join("Icons", f"Tile{num}.png")),
        (TILESIZE, TILESIZE)
    )
    tile_numbers.append(image)

# Carrega os restantes tiles (corretamente atribuídos)
tile_Empty     = pygame.transform.scale(pygame.image.load(os.path.join("Icons", "TileEmpty.png")),     (TILESIZE, TILESIZE))
tile_Exploded  = pygame.transform.scale(pygame.image.load(os.path.join("Icons", "TileExploded.png")),  (TILESIZE, TILESIZE))
tile_Flag      = pygame.transform.scale(pygame.image.load(os.path.join("Icons", "TileFlag.png")),      (TILESIZE, TILESIZE))
tile_Mine      = pygame.transform.scale(pygame.image.load(os.path.join("Icons", "TileMine.png")),      (TILESIZE, TILESIZE))
tile_NotMine   = pygame.transform.scale(pygame.image.load(os.path.join("Icons", "TileNotMine.png")),   (TILESIZE, TILESIZE))
tile_Unknown   = pygame.transform.scale(pygame.image.load(os.path.join("Icons", "TileUnknown.png")),   (TILESIZE, TILESIZE))
