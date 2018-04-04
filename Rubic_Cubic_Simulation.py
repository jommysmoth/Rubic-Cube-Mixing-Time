"""
Rubic Cube Simulation.

Starting basic rubic cube movement
"""
import numpy as np


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


def turn_cube_func(faces, turn_type, turn_axis):
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
            faces[0, :, :] = np.rot90(faces[0, :, :], 3)
        elif turn_axis == 2:
            faces[5, :, :] = np.rot90(faces[5, :, :], 3)
        turn_matrix[0, 1:4] = faces[1, turn_axis, :]
        turn_matrix[1:4, 4] = faces[2, turn_axis, :]
        turn_matrix[4, 1:4] = faces[3, turn_axis, :]
        turn_matrix[1:4, 0] = faces[4, turn_axis, :]
        turn_matrix = np.rot90(turn_matrix)
        faces[1, turn_axis, :] = turn_matrix[0, 1:4]
        faces[2, turn_axis, :] = turn_matrix[1:4, 4]
        faces[3, turn_axis, :] = turn_matrix[4, 1:4]
        faces[4, turn_axis, :] = turn_matrix[1:4, 0]
    if turn_type == 'l':
        # (1, 3) Turn, turns from 4 to 0 to 2 to 5 to 4
        if turn_axis == 0:
            faces[1, :, :] = np.rot90(faces[1, :, :], 3)
        elif turn_axis == 2:
            faces[3, :, :] = np.rot90(faces[3, :, :])
        turn_matrix[0, 1:4] = faces[5, :, turn_axis]
        turn_matrix[1:4, 4] = faces[2, :, turn_axis]
        turn_matrix[4, 1:4] = faces[0, :, turn_axis]
        turn_matrix[1:4, 0] = faces[4, :, ant_axis]
        turn_matrix = np.rot90(turn_matrix)
        faces[5, :, turn_axis] = turn_matrix[0, 1:4]
        faces[2, :, turn_axis] = turn_matrix[1:4, 4]
        faces[0, :, turn_axis] = np.flip(turn_matrix[4, 1:4], 0)
        faces[4, :, ant_axis] = turn_matrix[1:4, 0]
    if turn_type == 'w':
        if turn_axis == 0:
            faces[2, :, :] = np.rot90(faces[2, :, :], 3)
        elif turn_axis == 2:
            faces[4, :, :] = np.rot90(faces[4, :, :])
        turn_matrix[0, 1:4] = faces[0, ant_axis, :]
        turn_matrix[1:4, 4] = faces[3, :, turn_axis]
        turn_matrix[4, 1:4] = faces[5, turn_axis, :]
        turn_matrix[1:4, 0] = faces[1, :, ant_axis]
        turn_matrix = np.rot90(turn_matrix)
        faces[0, ant_axis, :] = turn_matrix[0, 1:4]
        faces[3, :, turn_axis] = turn_matrix[1:4, 4]
        faces[5, turn_axis, :] = turn_matrix[4, 1:4]
        faces[1, :, ant_axis] = turn_matrix[1:4, 0]
    return faces


if __name__ == '__main__':
    cube = generate_faces()
    movement_list = ['h', 'w', 'l']
    n_iter = 20
    for x in range(n_iter):
        m_type = movement_list[np.random.randint(3)]
        print(m_type)
        axis = np.random.randint(3)
        print(axis)
        cube = turn_cube_func(cube, m_type, axis)
    print(cube)
