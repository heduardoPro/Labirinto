import sys
import os
import pygame
from settings import BLACK, WHITE, WIDTH, HEIGHT

pygame.init()

icon_window = pygame.image.load('img/twitch_icon.png')
image_twitch = pygame.image.load('img/twitch.jpeg')
image_lulu = pygame.image.load('img/Lulu.png')

image_twitch = pygame.transform.scale(image_twitch, (40, 40))
image_lulu = pygame.transform.scale(image_lulu, (40, 40))


maze_file = "labirinto.txt"

def load_maze(file):
    maze = []
    with open(file, "r") as f:
        for row in f:
            maze.append(list(row.strip()))
    return maze

# Armazenando os dados arquivo.txt que contém as características do labirinto
maze_data = load_maze(maze_file)

def draw_maze(maze_data):
    for y, row in enumerate(maze_data):
        for x, cell in enumerate(row):
            if cell == "|": # Parede
                pygame.draw.rect(window, BLACK, (x * 40, y * 40, 40, 40))
            elif cell == "0": # Caminho
                pygame.draw.rect(window, WHITE, (x * 40, y * 40, 40, 40))
            elif cell == "M": # Twitch, rato ou inicio 
                position_twitch = (x, y)
                window.blit(image_twitch, (x * 40, y * 40))
            elif cell == "E": # Lulu, queijo ou fim 
                position_lulu = (x, y)
                window.blit(image_lulu, (x * 40, y * 40))


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labirinto do Twitch")
pygame.display.set_icon(icon_window)

status = True
while status:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False

    window.fill(WHITE)
    draw_maze(maze_data)
    pygame.display.update()

pygame.quit()
os.system('cls' if os.name == 'nt' else 'clear')
sys.exit()
