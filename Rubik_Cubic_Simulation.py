"""
Rubic Cube Simulation.

Starting basic rubic cube movement
"""
import numpy as np
import matplotlib.pyplot as plt


def generate_faces(rand=None):
    """
    Start.

    Used to make full or random faces (start with set)
    """
    faces = np.chararray((6, 3, 3), unicode=True, itemsize=8)
    colors = ['White', 'Green', 'Red', 'Blue', 'Orange', 'Yellow']
    for ind, color in enumerate(colors):
        faces[ind, :, :] = color
    """
    if isinstance(rand, int):
        continue
        # for iters in range(rand):
    """

    return faces


def turn_cube_func(faces, turn_type, turn_axis, rotate_amount):
    """
    Cube Movements.

    Keep a standard way to manipulate cube

    turn_type: 'w', 'l', 'h' for input, otherwise pushes error.

    turn_axis: 0, 1, 2 are a low to high standard of which to rotate.
    """
    turn_matrix = np.chararray((5, 5), unicode=True, itemsize=8)
    ant_axis = 2 - turn_axis
    if turn_type == 'h':
        # (0, 5) Turn, turns from 4 to 3 to 2 to 1 to 4
        if turn_axis == 0:
            faces[0, :, :] = np.rot90(faces[0, :, :], 3 + rotate_amount)
        elif turn_axis == 2:
            faces[5, :, :] = np.rot90(faces[5, :, :], 3 + rotate_amount)
        turn_matrix[0, 1:4] = faces[1, turn_axis, :]
        turn_matrix[1:4, 4] = faces[2, turn_axis, :]
        turn_matrix[4, 1:4] = faces[3, turn_axis, :]
        turn_matrix[1:4, 0] = faces[4, turn_axis, :]
        turn_matrix = np.rot90(turn_matrix, rotate_amount)
        faces[1, turn_axis, :] = turn_matrix[0, 1:4]
        faces[2, turn_axis, :] = turn_matrix[1:4, 4]
        faces[3, turn_axis, :] = turn_matrix[4, 1:4]
        faces[4, turn_axis, :] = turn_matrix[1:4, 0]
    if turn_type == 'l':
        # (1, 3) Turn, turns from 4 to 0 to 2 to 5 to 4
        if turn_axis == 0:
            faces[1, :, :] = np.rot90(faces[1, :, :], 3 + rotate_amount)
        elif turn_axis == 2:
            faces[3, :, :] = np.rot90(faces[3, :, :], rotate_amount)
        turn_matrix[0, 1:4] = faces[5, :, turn_axis]
        turn_matrix[1:4, 4] = faces[2, :, turn_axis]
        turn_matrix[4, 1:4] = faces[0, :, turn_axis]
        turn_matrix[1:4, 0] = faces[4, :, ant_axis]
        turn_matrix = np.rot90(turn_matrix, rotate_amount)
        faces[5, :, turn_axis] = turn_matrix[0, 1:4]
        faces[2, :, turn_axis] = turn_matrix[1:4, 4]
        faces[0, :, turn_axis] = np.flip(turn_matrix[4, 1:4], 0)
        faces[4, :, ant_axis] = turn_matrix[1:4, 0]
    if turn_type == 'w':
        if turn_axis == 0:
            faces[2, :, :] = np.rot90(faces[2, :, :], 3 + rotate_amount)
        elif turn_axis == 2:
            faces[4, :, :] = np.rot90(faces[4, :, :], rotate_amount)
        turn_matrix[0, 1:4] = faces[0, ant_axis, :]
        turn_matrix[1:4, 4] = faces[3, :, turn_axis]
        turn_matrix[4, 1:4] = faces[5, turn_axis, :]
        turn_matrix[1:4, 0] = faces[1, :, ant_axis]
        turn_matrix = np.rot90(turn_matrix, rotate_amount)
        faces[0, ant_axis, :] = turn_matrix[0, 1:4]
        faces[3, :, turn_axis] = turn_matrix[1:4, 4]
        faces[5, turn_axis, :] = turn_matrix[4, 1:4]
        faces[1, :, ant_axis] = turn_matrix[1:4, 0]
    return faces


def randomize_cube(cube, amount_shuffle, movement_list):
    """Randomize Cube x-amount."""
    size = len(movement_list)
    for x in range(amount_shuffle):
        m_type = movement_list[np.random.randint(size)]
        axis = np.random.randint(size)
        movement_amount = np.random.randint(size)
        cube = turn_cube_func(cube, m_type, axis, movement_amount)
    return cube


def find_sovled(number_shuffle, average_amount, overflow_amount, movement_list):
    """
    Finding Solved Cube.

    Assume solved cube face is a sufficiently random face, check other random faces in a function
    """
    cube = generate_faces()
    solved = np.copy(cube)
    solve_fin = 0
    overflow = 0
    solve_list = []
    ind_list = range(1, number_shuffle + 1)
    for it_am in range(1, number_shuffle + 1):
        print(it_am)
        solve_fin = 0
        overflow = 0
        for avg in range(average_amount):
            count = 0
            not_solved = True
            cube = generate_faces()
            cube = randomize_cube(cube, it_am, movement_list)
            while not_solved:
                count += 1
                cube = randomize_cube(cube, 1, movement_list)
                if np.array_equal(cube, solved):
                    not_solved = False
                    solve_fin += 1
                elif count > overflow_amount:
                    not_solved = False
                    overflow += 1
        solve_list.append(solve_fin)
    return solve_list, ind_list

if __name__ == '__main__':
    movement_list = ['h', 'w', 'l']
    fig = plt.figure()
    fig_2d = plt.figure()
    ax = fig.add_subplot(111)
    ax_2d = fig_2d.add_subplot(111)
    n_iter = 20
    averages = 1000
    overflow_amount = 1000
    average_list = [100, 1000]
    for averages in average_list:
        solve_list, ind_list = find_sovled(n_iter, averages, overflow_amount, movement_list)
        solve_list = [x / averages for x in solve_list]
        solve_list_2d, ind_list_2d = find_sovled(n_iter, averages, overflow_amount, ['h', 'w'])
        solve_list_2d = [x / averages for x in solve_list_2d]
        if averages == average_list[0]:
            col = 'go-'
        if averages == average_list[1]:
            col = 'bo-'
        ax.plot(ind_list, solve_list, col)
        ax_2d.plot(ind_list_2d, solve_list_2d, col)
    ax.set_xticks(ind_list)
    ax_2d.set_xticks(ind_list_2d)
    ax.set_title('For %i random shufflings of random cube,'
                 ' with %i as overflow amount (3d Full Set)' % (n_iter, overflow_amount))
    ax_2d.set_title('For %i random shufflings of random cube,'
                    ' with %i as overflow amount (2d Restricted)' % (n_iter, overflow_amount))
    ax.set_xlabel('Amount of iterations')
    ax_2d.set_xlabel('Amount of iterations')
    ax.set_ylabel('Amount of times reaches starting state (Normalized)')
    ax_2d.set_ylabel('Amount of times reaches starting state (Normalized)')
    ax.legend(average_list)
    ax_2d.legend(average_list)
    plt.show()
