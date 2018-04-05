"""
Rubic Cube Simulation.

Starting basic rubic cube movement
"""
import numpy as np
import matplotlib.pyplot as plt


def generate_faces():
    """
    Start.

    Used to make full or random faces (start with set)
    """
    faces = np.chararray((6, 3, 3), unicode=True, itemsize=8)
    colors = ['White', 'Green', 'Red', 'Blue', 'Orange', 'Yellow']
    for ind, color in enumerate(colors):
        faces[ind, :, :] = color

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


def randomize_cube(cube, amount_shuffle):
    """Randomize Cube x-amount."""
    for x in range(amount_shuffle):
        m_type = movement_list[np.random.randint(3)]
        axis = np.random.randint(3)
        movement_amount = np.random.randint(3)
        cube = turn_cube_func(cube, m_type, axis, movement_amount)
    return cube


def find_sovled(number_shuffle, average_amount, overflow_amount):
    """
    Finding Solved Cube.

    Assume solved cube face is a sufficiently random face, check other random faces in a function
    """
    cube = generate_faces()
    solved = np.copy(cube)
    solve_fin = 0
    overflow = 0
    solve_list = []
    ind_list = range(1, n_iter + 1)
    for it_am in range(1, n_iter + 1):
        print(it_am)
        for avg in range(averages):
            count = 0
            not_solved = True
            cube = generate_faces()
            cube = randomize_cube(cube, it_am)
            while not_solved:
                count += 1
                cube = randomize_cube(cube, 1)
                if np.array_equal(cube, solved):
                    not_solved = False
                    solve_fin += 1
                elif count > overflow_amount:
                    not_solved = False
                    overflow += 1
        solve_list.append(solve_fin)
    return solve_list, ind_list


def find_rand(number_shuffle, average_amount, overflow_amount):
    """
    Finding Solved Cube.

    Assume solved cube face is a sufficiently random face, check other random faces in a function
    """
    cube = generate_faces()
    solved = np.copy(cube)
    solve_fin = 0
    overflow = 0
    solve_list = []
    ind_list = range(1, n_iter + 1)
    for it_am in range(1, n_iter + 1):
        print(it_am)
        for avg in range(averages):
            count = 0
            not_solved = True
            cube = generate_faces()
            # print(cube)
            for x in range(it_am):
                m_type = movement_list[np.random.randint(3)]
                axis = np.random.randint(3)
                movement_amount = np.random.randint(3)
                cube = turn_cube_func(cube, m_type, axis, movement_amount)
            while not_solved:
                count += 1
                m_type = movement_list[np.random.randint(3)]
                axis = np.random.randint(3)
                cube = turn_cube_func(cube, m_type, axis, movement_amount)
                if np.array_equal(cube, solved):
                    not_solved = False
                    solve_fin += 1
                elif count > overflow_amount:
                    not_solved = False
                    overflow += 1
        solve_list.append(solve_fin)
    return solve_list, ind_list


if __name__ == '__main__':
    # cube = generate_faces()
    # solved = np.copy(cube)
    movement_list = ['h', 'w', 'l']
    n_iter = 15
    averages = 1000
    overflow_amount = 100
    solve_list, ind_list = find_sovled(n_iter, averages, overflow_amount)
    plt.plot(ind_list, solve_list, 'ko-')
    plt.xticks(ind_list)
    plt.title('For %i random shufflings of random cube,'
              ' with %i as overflow amount' % (n_iter, overflow_amount))
    plt.xlabel('Amount of iterations')
    plt.ylabel('Amount of times, out of %i, reaches starting state' % averages)
    plt.show()
