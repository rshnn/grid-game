
def move(position, grid, direction, count):
    if direction in 'U D L R'.split():
        return move_cartesian(position, grid, direction, count)
    if direction in 'UR UL DR DL'.split():
        return move_diagonal(position, grid, direction, count)
    else: 
        raise Exception('Invalid direction provided')



def move_cartesian(position, grid, direction, count):
    x, y = position
    dimension = len(grid.grid)
    out_grid = np.copy(grid.grid) 

    if direction == 'U':
        y1 = y - 1
        y2 = y - 2
        y3 = y - 3

        out_grid[x, y1] = count
        out_grid[x, y2] = count
        out_grid[x, y3] = count
        position = [x, y3]

        return position, out_grid   


    if direction == 'D':
        y1 = y + 1
        y2 = y + 2
        y3 = y + 3

        out_grid[x, y1] = count
        out_grid[x, y2] = count
        out_grid[x, y3] = count
        position = [x, y3]

        return position, out_grid   


    if direction == 'R':
        x1 = x + 1
        x2 = x + 2
        x3 = x + 3

        out_grid[x1, y] = count
        out_grid[x2, y] = count
        out_grid[x3, y] = count
        position = [x3, y]

        return position, out_grid   


    if direction == 'L':
        x1 = x - 1
        x2 = x - 2
        x3 = x - 3

        out_grid[x1, y] = count
        out_grid[x2, y] = count
        out_grid[x3, y] = count
        position = [x3, y]

        return position, out_grid   

    else: 
        raise Exception("invalid cartesian direction")


def move_diagonal(position, grid, direction, count):
    x, y = position
    dimension = len(grid.grid)
    out_grid = np.copy(grid.grid) 


    if direction == 'UL':
        x1 = x - 1 
        x2 = x - 2 
        y1 = y - 1
        y2 = y - 2

    if direction == 'UR':
        x1 = x + 1 
        x2 = x + 2 
        y1 = y - 1
        y2 = y - 2

    if direction == 'DR':
        x1 = x + 1 
        x2 = x + 2 
        y1 = y + 1
        y2 = y + 2

    if direction == 'DL':
        x1 = x - 1 
        x2 = x - 2 
        y1 = y + 1
        y2 = y + 2

    else: 
        raise Exception('Invalid diagonal direction')

    out_grid[x1, y1] = count
    out_grid[x2, y2] = count
    position = [x2, y2]

    return position, out_grid   
