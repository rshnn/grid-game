

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


    if direction == 'U':
        y1 = y - 1
        y2 = y - 2
        y3 = y - 3
        if all(0 <= y < dimension for y in [y1, y2, y3]): 
            if all(grid.can_i_move_here([x, y]) for y in [y1, y2, y3]):
                return True 
            else: 
                return False 
        else: 
            return False 


    if direction == 'D':
        y1 = y + 1
        y2 = y + 2
        y3 = y + 3
        if all(0 <= y < dimension for y in [y1, y2, y3]): 
            if all(grid.can_i_move_here([x, y]) for y in [y1, y2, y3]):
                return True   

            else: 
                return False 
        else: 
            return False 


    if direction == 'R':
        x1 = x + 1
        x2 = x + 2
        x3 = x + 3
        if all(0 <= x < dimension for x in [x1, x2, x3]): 
            if all(grid.can_i_move_here([x, y]) for x in [x1, x2, x3]):
                return True  

            else: 
                return False 
        else: 
            return False 


    if direction == 'L':
        x1 = x - 1
        x2 = x - 2
        x3 = x - 3
        if all(0 <= x < dimension for x in [x1, x2, x3]): 
            if all(grid.can_i_move_here([x, y]) for x in [x1, x2, x3]):
                return True   

            else: 
                return False 
        else: 
            return False 

    else: 
        raise Exception("invalid cartesian direction")

def move_diagonal(position, grid, direction):
    x, y = position
    dimension = len(grid.grid)


    if direction == 'UL':
        x1 = x - 1 
        x2 = x - 2 
        y1 = y - 1
        y2 = y - 2

        if all(0 <= x < dimension for x in [x1, x2, y1, y2]):
            if all(grid.can_i_move_here(coords) for coords in [[x1, y1], [x2, y2]]):
                return True  

            else:
                return False 
        else: 
            return False 

    if direction == 'UR':
        x1 = x + 1 
        x2 = x + 2 
        y1 = y - 1
        y2 = y - 2

        if all(0 <= x < dimension for x in [x1, x2, y1, y2]):
            if all(grid.can_i_move_here(coords) for coords in [[x1, y1], [x2, y2]]):
                return True  

            else:
                return False 
        else: 
            return False 

    if direction == 'DR':
        x1 = x + 1 
        x2 = x + 2 
        y1 = y + 1
        y2 = y + 2

        if all(0 <= x < dimension for x in [x1, x2, y1, y2]):
            if all(grid.can_i_move_here(coords) for coords in [[x1, y1], [x2, y2]]):
                return True  
                
            else:
                return False 
        else: 
            return False 


    if direction == 'DL':
        x1 = x - 1 
        x2 = x - 2 
        y1 = y + 1
        y2 = y + 2

        if all(0 <= x < dimension for x in [x1, x2, y1, y2]):
            if all(grid.can_i_move_here(coords) for coords in [[x1, y1], [x2, y2]]):
                return True  
                
            else:
                return False 
        else: 
            return False 

    else: 
        raise Exception('Invalid diagonal direction')
