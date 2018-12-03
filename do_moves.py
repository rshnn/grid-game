import numpy as np 


def move(position, grid, direction, count):
    if direction in 'U D L R'.split():
        return move_cartesian(position, grid, direction, count)
    if direction in 'UR UL DR DL'.split():
        return move_diagonal(position, grid, direction, count)
    else: 
        raise Exception('Invalid direction provided')



def move_cartesian(position, grid, direction, count):
    x, y = position
    out_grid = np.copy(grid.grid) 

    if direction == 'L':
        y3 = y - 3

        out_grid[x, y3] = count
        position = [x, y3]

        return position, out_grid   


    if direction == 'R':
        y3 = y + 3

        out_grid[x, y3] = count
        position = [x, y3]

        return position, out_grid   


    if direction == 'D':
        x3 = x + 3

        out_grid[x3, y] = count
        position = [x3, y]

        return position, out_grid   


    if direction == 'U':
        x3 = x - 3

        out_grid[x3, y] = count
        position = [x3, y]

        return position, out_grid   

    else: 
        raise Exception("invalid cartesian direction")


def move_diagonal(position, grid, direction, count):
    x, y = position
    out_grid = np.copy(grid.grid) 


    if direction == 'UL':
        x2 = x - 2 
        y2 = y - 2

    elif direction == 'DL':
        x2 = x + 2 
        y2 = y - 2

    elif direction == 'DR':
        x2 = x + 2 
        y2 = y + 2

    elif direction == 'UR':
        x2 = x - 2 
        y2 = y + 2

    else: 
        raise Exception('Invalid diagonal direction')

    out_grid[x2, y2] = count
    position = [x2, y2]

    return position, out_grid   
