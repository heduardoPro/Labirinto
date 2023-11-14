import pygame
import os
import sys
import time
from settings import *
from functions.load_maze import load_maze_file
from functions.draw_maze import draw
from functions.positions import find_position_twitch, find_position_lulu

from stack import Stack

pygame.init()
pygame.mixer.init()

# Carregar imagens
twitch_image = pygame.image.load("assets/twitch.png")
lulu_image = pygame.image.load("assets/lulu.png")
lol_icon = pygame.image.load("assets/League_of_Legends_icon.webp")

twitch_image = pygame.transform.scale(twitch_image, (CELL_SIZE, CELL_SIZE))
lulu_image = pygame.transform.scale(lulu_image, (CELL_SIZE, CELL_SIZE))

# Sons
pygame.mixer.music.load("assets/sound/initial.mp3")
som_souEU = pygame.mixer.Sound("assets/sound/souEU.mp3")
som_souEU.set_volume(0.5)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("League of Labyrinths")
pygame.display.set_icon(lol_icon)

status = True

while status:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False

        # Atualize a tela
        screen.fill(WHITE)
        pygame.display.flip()
        time.sleep(0.3)

pygame.quit()
os.system('cls' if os.name == 'nt' else 'clear')
sys.exit()
