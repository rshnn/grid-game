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
        self.current_position = [np.nan, np.nan]


    def set_current(self, row, col):
        self.current_position = [row, col]
        self.grid[self.current_position] = 1


    def print(self):
        print(self.grid)


    def can_i_move_here(self, coords):
        if self.grid[coords[0], coords[1]] > 0:
            return False
        else: 
            return True 
