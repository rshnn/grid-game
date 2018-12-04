from state import State 
import seaborn as sns 
import numpy as np 


def recursive_run(state, solved):

    if state.grid.solved(): 
        return True, state, solved

    else: 
        for direction in "U L D R UR UL DR DL".split():
            if state.is_move_possible(direction) is False:
                continue
            else: 
                new_state = state.apply_move(direction)
                out, s, solved = recursive_run(new_state, solved)
                if out is False: 
                    continue
                else: 
                    solved.append(s)
                    continue

    return False, state, solved


def try_run(starting_coords):
    s0 = State(starting_coords)
    out, state, solved = recursive_run(s0, [])
    return out, state, solved


def solve_for_solutions(log=True):
    solved = []

    for i in range(5):
        for j in range(5):
            if log: 
                print("Solving for initial coords: ({}, {})...".format(i, j), end='')

            out, final_state, solution_states = try_run([i, j])

            if log: 
                print('done')

            solved.append(([i, j], solution_states))

    return solved 


def plot_solved_grid(grid, title='Solution plot, whoop'):
    fig = sns.heatmap(grid, annot=True)
    fig.figure.axes[0].set_title(title)
    return fig 


def plot_some_random_solution_idc_which_one(solutions):

    i = np.random.randint(0, len(solutions))
    j = np.random.randint(0, len(solutions[i][1]))
    initial_coords = solutions[i][0]

    title = "Starting coords: ({}, {}), solution #{} out of {}".format(initial_coords[0], 
                                                                       initial_coords[1], 
                                                                       j, 
                                                                       len(solutions[i][1])
                                                                       )
    grid = solutions[i][1][j].grid.grid
    figure = plot_solved_grid(grid, title)
    return figure 
