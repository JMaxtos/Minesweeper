from constants import TILESIZE
import os
import pygame
tile_numbers =[]
for num in range(1,9):
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("Icons",f"Tile{num}.png")),(TILESIZE,TILESIZE)))

tile_empty = tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("Icons","TileEmpty.png")),(TILESIZE,TILESIZE)))
tile_exploded = tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("Icons","TileExploded.png")),(TILESIZE,TILESIZE)))
tile_flag = tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("Icons","TileFlag.png")),(TILESIZE,TILESIZE)))
tile_mine = tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("Icons","TileMine.png")),(TILESIZE,TILESIZE)))
tile_notMine = tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("Icons","TileNotMine.png")),(TILESIZE,TILESIZE)))
tile_Unknown = tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("Icons","TileUnknown.png")),(TILESIZE,TILESIZE)))
