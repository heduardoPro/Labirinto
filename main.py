import pygame
import sys
import time
from settings import *
from functions.load_maze import load_maze_file
from functions.positions import find_position_twitch, find_position_lulu

pygame.init()
pygame.mixer.init()

# Carregar imagens
twitch = pygame.image.load("assets/twitch.png")
lulu = pygame.image.load("assets/lulu.png")
lol_icon = pygame.image.load("assets/League_of_Legends_icon.webp")

twitch_image = pygame.transform.scale(twitch, (CELL_SIZE, CELL_SIZE))
lulu_image = pygame.transform.scale(lulu, (CELL_SIZE, CELL_SIZE))

# Sons
pygame.mixer.music.load("assets/sound/initial.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("League of Labyrinths")
pygame.display.set_icon(lol_icon)

# maze_data = load_maze_file("vitor.txt")
# maze_data = load_maze_file("maze.txt")
maze_data = load_maze_file("willian.txt")
# maze_data = load_maze_file("lucas.txt")

twitch_start_x, twitch_start_y = find_position_twitch(maze_data)
lulu_end_x, lulu_end_y = find_position_lulu(maze_data)

def draw(screen, maze_data, lulu_image, twitch_x, twitch_y, lulu_x, lulu_y):
    screen.fill(WHITE)
    for row in range(len(maze_data)):
        for column in range(len(maze_data[row])):
            cell = maze_data[row][column]
            if cell == "1":  # Parede
                pygame.draw.rect(screen, BLACK, (column * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == "0":  # Caminho
                pygame.draw.rect(screen, WHITE, (column * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == "M":
                screen.blit(twitch_image, (twitch_x * CELL_SIZE, twitch_y * CELL_SIZE))
            elif cell == "E":
                screen.blit(lulu_image, (lulu_x * CELL_SIZE, lulu_y * CELL_SIZE))

def draw_path(screen, path, color):
    for position in path:
        pygame.draw.rect(screen, color, (position[0] * CELL_SIZE, position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def backtracking(maze_data, twitch_position_x, twitch_position_y, lulu_position_x, lulu_position_y):
    paths_visited = []
    right_route = []

    def position_is_valid(location_x, location_y):
        return 0 <= location_x < len(maze_data[0]) and 0 <= location_y < len(maze_data)

    while (twitch_position_x, twitch_position_y) != (lulu_position_x, lulu_position_y):
        position = (twitch_position_x, twitch_position_y)

        # verifica se é possivel mover para direita
        # verifica se a próxima posição contém um caminho livre "0" ou se já é a posição da lulu(saída) "E" nao permite que o proximo movimento seja um caminho visitado
        if position_is_valid(twitch_position_x + 1, twitch_position_y) and maze_data[twitch_position_y][twitch_position_x + 1] in ["0", "E"] and (twitch_position_x + 1, twitch_position_y) not in paths_visited:
            twitch_position_x += 1
            # Empilha o movimento nas pilhas 
            paths_visited.append((twitch_position_x, twitch_position_y))
            right_route.append(position)

        # Esquerda
        elif position_is_valid(twitch_position_x - 1, twitch_position_y) and maze_data[twitch_position_y][twitch_position_x - 1] in ["0", "E"] and (twitch_position_x - 1, twitch_position_y) not in paths_visited:
            twitch_position_x -= 1
            paths_visited.append((twitch_position_x, twitch_position_y))
            right_route.append(position)

        # Baixo 
        elif position_is_valid(twitch_position_x, twitch_position_y + 1) and maze_data[twitch_position_y + 1][twitch_position_x] in ["0", "E"] and (twitch_position_x, twitch_position_y + 1) not in paths_visited:
            twitch_position_y += 1
            paths_visited.append((twitch_position_x, twitch_position_y))
            right_route.append(position)

        # Cima
        elif position_is_valid(twitch_position_x, twitch_position_y - 1) and maze_data[twitch_position_y - 1][twitch_position_x] in ["0", "E"] and (twitch_position_x, twitch_position_y - 1) not in paths_visited:
            twitch_position_y -= 1
            paths_visited.append((twitch_position_x, twitch_position_y))
            right_route.append(position)
        else:
            if not right_route:
                break  # Evita o pop de lista vazia
            last_position = right_route.pop()
            twitch_position_x, twitch_position_y = last_position

    return right_route, paths_visited

visiteds_path_stack = [] 
correct_path_stack = []  

status = True

while status:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False

    if status:
        draw(screen=screen, maze_data=maze_data, twitch_x=twitch_start_x, twitch_y=twitch_start_y,  lulu_image=lulu_image, lulu_x=lulu_end_x, lulu_y=lulu_end_y)
        pygame.display.flip()
        time.sleep(0.1)
        status = False

    correct_path, visiteds_path = backtracking(maze_data, twitch_start_x, twitch_start_y, lulu_end_x, lulu_end_y)
    if len(correct_path) > 0 or len(visiteds_path) > 0:

        for path in visiteds_path:
            visiteds_path_stack.append(path)  # Adiciona a posição que o twitch passou à pilha de caminhos visitados
            draw_path(screen, [path], RED)
            pygame.display.flip()
            time.sleep(0.1)

        for path in correct_path:
            correct_path_stack.append(path)  # pilha do caminho correto
            draw_path(screen, [path], GREEN)
            pygame.display.flip()
            time.sleep(0.1)

        twitch_x, twitch_y = correct_path[-1] if len(correct_path) < 0 else visiteds_path[-1]
        screen.blit(twitch_image, (twitch_x * CELL_SIZE, twitch_y * CELL_SIZE))
        pygame.display.flip()

        time.sleep(0.1)  


print("Caminho Correto:")
for position in correct_path_stack:
    print(position)

print("\nCaminhos Visitados:")
for position in visiteds_path_stack:
    print(position)

pygame.quit()
sys.exit()

