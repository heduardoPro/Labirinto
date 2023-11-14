def find_position_twitch(maze_data):
    for row in range(len(maze_data)):
        for cell in range(len(maze_data[row])):
            if maze_data[row][cell] == 'M':
                return row, cell
            
def find_position_lulu(maze_data):
    for row in range(len(maze_data)):
        for cell in range(len(maze_data[row])):
            if maze_data[row][cell] == 'E':
                return row, cell
