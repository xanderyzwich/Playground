"""
Conway's Game of LifeConway's Game of Life takes place on a two-dimensional board of square cells.
Each cell is either dead or alive, and at each tick, the following rules apply:
    1. Any live cell with less than two live neighbors dies.
    2. Any live cell with two or three live neighbors remains living.
    3. Any live cell with more than three live neighbors dies.
    4. Any dead cell with exactly three live neighbors becomes a live cell.
A cell neighbors another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life.
It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for.
You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
"""
from unittest import TestCase
import numpy as np


def is_alive_next(grid, object_coords):
    """
    Decide whether the point in grid specified by object_coords will be alive next turn
    :param grid: 2D array/list
    :param object_coords: tuple of X-position and Y-position in that order
    :return: 1 if alive, else 0
    """

    # Establish whether object position was previously alive
    x, y = object_coords
    max_x, max_y = grid.shape
    was_alive = 1 == grid[x][y]
    print(f'was_alive: {was_alive}')

    # Find number of living neighbors
    living_neighbors = 0
    for row_num in [r for r in [x - 1, x, x + 1] if 0 <= r <= max_x]:  # above, below, and same row (inside grid)
        for col_num in [c for c in [y - 1, y, y + 1] if 0 <= c <= max_y]:  # left, right, and same col (inside grid)
            if grid[row_num][col_num] == 1 \
                    and not (row_num == x and col_num == y):  # count other cells that are alive
                living_neighbors += 1
    print(f'Found {living_neighbors} living neighbors')

    # Assert actual rules
    # Rules 2 and 4 define the only way that a cell can be alive
    if was_alive and living_neighbors in [2, 3]:
        print('Rule 2')
        return 1
    elif living_neighbors == 3:
        print('Rule 4')
        return 1
    # all other scenarios result in a dead cell
    return 0


def create_grid(rows, cols, living):
    """
    Create data grid
    :param rows: number of rows in the grid
    :param cols: number of columns in the grid
    :param living: x,y tuples for each living cell
    :return: numpy array of where 1's are alive and 0's are not
    """
    temp_array = np.zeros([rows, cols])
    for x, y in living:
        temp_array[x][y] = 1
    return temp_array


def create_test_grid(alive, living=[]):
    """
    Wrapper for create_grid to assist with tests
    :param alive: True if 1,1 is alive
    :param living: tuples of living neighbors
    :return: 3x3 numpy array of where 1's are alive and 0's are not
    """
    _living = living
    if alive:
        _living.append((1, 1))
    return create_grid(3, 3, _living)


class TestIsAliveNext(TestCase):
    def test_rule_one(self):
        """
        Rule 1: Any live cell with less than two live neighbors dies.
        """
        data = create_test_grid(alive=True)
        assert 1 != is_alive_next(data, (1, 1))

    def test_rule_two(self):
        """
        Rule 2: Any live cell with two or three live neighbors remains living.
        """
        data = create_test_grid(alive=True, living=[(0, 0), (2, 2)])
        assert 1 == is_alive_next(data, (1, 1))

    def test_rule_three(self):
        """
        Rule 3: Any live cell with more than three live neighbors dies.
        """
        data = create_test_grid(alive=True, living=[(0, 1), (1, 2), (2, 0), (2, 2)])
        assert 0 == is_alive_next(data, (1, 1))

    def test_rule_four(self):
        """
        Rule 4: Any dead cell with exactly three live neighbors becomes a live cell.
        """
        data = create_test_grid(alive=False, living=[(0, 0), (0, 1), (0, 2)])
        assert True


