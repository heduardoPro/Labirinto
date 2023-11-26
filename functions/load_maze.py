def load_maze_file(filename):
    maze_list = []
    with open(filename, "r") as file:
        text = file.readline()
        text = text.split(" ")
        for line in file:
            maze_list.append(list(line.strip()))
        return maze_list

"""
maze_file = "maze.txt"
maze_data = load_maze_file(maze_file)

twitch_start_x, twitch_start_y = find_position_twitch(maze_data)
lulu_end_x, lulu_end_y = find_position_lulu(maze_data)

print(twitch_start_x, twitch_start_y)
print(lulu_end_x, lulu_end_y)
"""