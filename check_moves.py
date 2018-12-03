
def check(position, grid, direction):
    if direction in 'U D L R'.split():
        return check_cartesian(position, grid, direction)
    if direction in 'UR UL DR DL'.split():
        return check_diagonal(position, grid, direction)
    else: 
        raise Exception('Invalid direction provided')


def check_cartesian(position, grid, direction):
    x, y = position
    dimension = len(grid.grid)

    if direction == 'L':
        y1 = y - 3

        if 0 <= y1 < dimension: 
            if grid.can_i_move_here([x, y1]):
                return True 
            else: 
                return False 
        else: 
            return False 


    if direction == 'R':
        y1 = y + 3

        if 0 <= y1 < dimension: 
            if grid.can_i_move_here([x, y1]):
                return True 
            else: 
                return False 
        else: 
            return False 


    if direction == 'D':
        x1 = x + 3

        if 0 <= x1 < dimension: 
            if grid.can_i_move_here([x1, y]):
                return True 
            else: 
                return False 
        else: 
            return False 


    if direction == 'U':
        x1 = x - 3

        if 0 <= x1 < dimension: 
            if grid.can_i_move_here([x1, y]):
                return True 
            else: 
                return False 
        else: 
            return False 

    else: 
        raise Exception("invalid cartesian direction")


def check_diagonal(position, grid, direction):
    x, y = position
    dimension = len(grid.grid)

    if direction == 'UL':
        x1 = x - 2 
        y1 = y - 2

        if all(0 <= coord < dimension for coord in [x1, y1]):
            if grid.can_i_move_here([x1, y1]):
                return True  

            else:
                return False 
        else: 
            return False 

    if direction == 'DL':
        x1 = x + 2 
        y1 = y - 2

        if all(0 <= coord < dimension for coord in [x1, y1]):
            if grid.can_i_move_here([x1, y1]):
                return True  

            else:
                return False 
        else: 
            return False 

    if direction == 'DR':
        x1 = x + 2 
        y1 = y + 2

        if all(0 <= coord < dimension for coord in [x1, y1]):
            if grid.can_i_move_here([x1, y1]):
                return True  

            else:
                return False 
        else: 
            return False 


    if direction == 'UR':
        x1 = x - 2 
        y1 = y + 2

        if all(0 <= coord < dimension for coord in [x1, y1]):
            if grid.can_i_move_here([x1, y1]):
                return True  

            else:
                return False 
        else: 
            return False 

    else: 
        raise Exception('Invalid diagonal direction')
