import numpy as np 
from run import Run 


class GameMap():
    """
        5x5 square
        Starting at any point, fill in 0s with 1s
        Cartesian move = 3 spaces 
        Diagonal move = 2 spaces
    """

    def __init__(self, dimension):
        self.grid = np.zeros([dimension, dimension])
        self.dimension = dimension


    def reset(self):
        self.grid = np.zeros([self.dimension, self.dimension])


    def print(self):
        print(self.grid.transpose())


    def can_i_move_here(self, coords):
        if self.grid[coords[0], coords[1]] > 0:
            return False
        else: 
            return True 


    def solved(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.grid[i,j] == 0:
                    return False 
        else: 
            return True 


    def recursive_run(self, run):

        if(self.solved is True):
            print('~wtf pass!')
            return run.path

        else:
            for direction in 'U D L R UR UL DR DL'.split():
                if run.move(direction) is not False: 
                    print(direction)
                    self.print()
                    print()
                    return self.recursive_run(run)


        print("all failed.  path: {}".format(run.path))
        return run.path  


    def try_run(self, starting_coords):
        run = Run(self, starting_coords)  
        path =  self.recursive_run(run)  
        print(path)
        return 


