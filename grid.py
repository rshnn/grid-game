import numpy as np 


class Grid():
    """
        5x5 square
        Starting at any point, fill in 0s with 1s
        Cartesian move = 3 spaces 
        Diagonal move = 2 spaces
    """

    def __init__(self, dimension):
        self.grid = np.zeros([dimension, dimension])
        self.dimension = dimension


    def set_current(self, position, count):
        self.grid[position[0], position[1]] = count


    def print(self):
        print(self.grid)


    def can_i_move_here(self, coords):
        if self.grid[coords[0], coords[1]] > 0:
            return False
        else: 
            return True 


    def solved(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.grid[i, j] == 0:
                    return False 
        else: 
            return True 
