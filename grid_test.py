import numpy as np 
from run import Run 
from game_map import GameMap 


DIMENSION = 5


def recursive_run(run, prev=None, skip=None):

    print('CALL')
    prev_run = copy_of_run(run)

    if(run.map.solved is True):
        print('~wtf pass!')
        return run.path

    else:

        for direction in 'U D L R UR UL DR DL'.split():
            if direction == skip: 
                continue 

            if run.move(direction) is not False: 
                print(direction)
                run.map.print()
                print()
                out = recursive_run(run, prev_run)
                if out is not None: 
                    return out 
                else: 
                    run.path = " ".join(run.path.split()[0:-1])
                    continue 
            else: 
                print('cannot move in {}'.format(direction))


        # if all fail, backtrack 
        if run.count > 1 and prev is not None: 
            prev.map.print()
            print("prev", prev.path)
            print("run", run.path)
            return recursive_run(prev, None, run.path.split()[-1])


    print("all failed.  path: {}".format(run.path))
    run.map.print()
    print()
    return None  


def try_run(starting_coords):
    run = Run(starting_coords, DIMENSION)  

    path = recursive_run(run)
    return path 


def copy_of_run(run):
    position = run.current_position 
    dimension = run.dimension
    
    new_run = Run(position, dimension)

    new_run.count = run.count 
    new_run.map.grid = np.copy(run.map.grid) 
    new_run.path = run.path 

    return new_run
