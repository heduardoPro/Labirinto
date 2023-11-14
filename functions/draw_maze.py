import pygame
from settings import BLACK, WHITE, CELL_SIZE

def draw(screen, maze_data, lulu_image, lulu_x, lulu_y):
    for row in range(len(maze_data)):
        for cell in range(len(maze_data[row])):
            if cell == "1":  # Parede
                pygame.draw.rect(screen, BLACK, (cell * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == "0":  # Caminho
                pygame.draw.rect(screen, WHITE, (cell * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == "E":
                pygame.blit(lulu_image, (lulu_x * CELL_SIZE, lulu_y * CELL_SIZE))