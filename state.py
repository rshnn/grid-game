import numpy as np 
from grid import Grid 
import check_moves
import do_moves 

DIMENSION = 4


class State():
    """A state in the search space.  
    Consists of: 
        grid 
        position
        count 
    """

    def __init__(self, position, grid_state=None, count=1, path=[]):
        """Returns a state with a new Grid instance.  
        """
        self.grid = Grid(DIMENSION)

        self.position = position 
        self.grid.set_current(position, count)
        self.count = count + 1 
        self.path = path

        # Inheriting an old grid state  
        if grid_state is not None: 
            self.grid.grid = grid_state
            self.count = count 


    def apply_move(self, direction):
        """Returns a new State instance with move applied 
        """
        if self.is_move_possible(direction):
            position, grid = do_moves.move(self.position, 
                                           self.grid, direction, self.count) 

            new_path = self.path + [direction]
            return State(position, grid, self.count + 1, new_path)

        else:
            raise Exception('Illegal move {}.'.format(direction)) 


    def is_move_possible(self, direction):
        """Returns boolean.  
            Operates over grid and position to see if direction is a valid move
            Does NOT mutate any structures  
        """
        return check_moves.check(self.position, self.grid, direction)
