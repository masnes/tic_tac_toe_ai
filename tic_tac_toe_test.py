import tic_tac_toe
import itertools


def debug_node():
    board_array = [[0 for x in range(3)] for x in range(3)]
    print(board_array)
    parent = tic_tac_toe.Node(None, board_array, 1)
    children_arrays = []
    for i in range(3):
        for j in range(3):
            new_board = [[0 for x in range(3)] for x in range(3)]
            new_board[i][j] = 1
            children_arrays.append(new_board)
    for child_array in children_arrays:
        child_node = tic_tac_toe.Node(parent, child_array, 1)
        parent.add_child(child_node)

    print(parent.children)
    for child in parent.children:
        print(child.board_array)
        print(child.winner)
    print(parent.board_array)
    print(parent.winner)


# format: board, check, horizontal_check, vertical_check, diagonal_check
known_values = (([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 0], [0, 0, 1]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 0], [0, 0, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 0], [0, 1, 1]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 0], [0, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 0], [0, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 0], [1, 1, 1]], 1, 1, 0, 0),
                ([[0, 0, 0], [0, 0, 0], [1, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 0], [1, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 0], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 0, 0], [0, 0, 1], [0, 0, 1]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 1], [0, 0, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 1], [0, 1, 1]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 1], [0, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 1], [0, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 1], [1, 1, 1]], 1, 1, 0, 0),
                ([[0, 0, 0], [0, 0, 1], [1, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 1], [1, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 1], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 0, 0], [0, 0, 2], [0, 0, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 2], [0, 1, 1]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 2], [0, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 2], [0, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 2], [1, 1, 1]], 1, 1, 0, 0),
                ([[0, 0, 0], [0, 0, 2], [1, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 2], [1, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 0, 2], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 0, 0], [0, 1, 1], [0, 1, 1]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 1, 1], [0, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 1, 1], [0, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 1, 1], [1, 1, 1]], 1, 1, 0, 0),
                ([[0, 0, 0], [0, 1, 1], [1, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 1, 1], [1, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 1, 1], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 0, 0], [0, 1, 2], [0, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 1, 2], [0, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 1, 2], [1, 1, 1]], 1, 1, 0, 0),
                ([[0, 0, 0], [0, 1, 2], [1, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 1, 2], [1, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 1, 2], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 0, 0], [0, 2, 2], [0, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 2, 2], [1, 1, 1]], 1, 1, 0, 0),
                ([[0, 0, 0], [0, 2, 2], [1, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 2, 2], [1, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [0, 2, 2], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 0, 0], [1, 1, 1], [1, 1, 1]], 1, 1, 0, 0),
                ([[0, 0, 0], [1, 1, 1], [1, 1, 2]], 1, 1, 0, 0),
                ([[0, 0, 0], [1, 1, 1], [1, 2, 2]], 1, 1, 0, 0),
                ([[0, 0, 0], [1, 1, 1], [2, 2, 2]], 1, 1, 0, 0),
                ([[0, 0, 0], [1, 1, 2], [1, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [1, 1, 2], [1, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [1, 1, 2], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 0, 0], [1, 2, 2], [1, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 0], [1, 2, 2], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 0, 0], [2, 2, 2], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 0, 1], [0, 0, 1], [0, 0, 1]], 1, 0, 1, 0),
                ([[0, 0, 1], [0, 0, 1], [0, 0, 2]], 0, 0, 0, 0),
                ([[0, 0, 1], [0, 0, 1], [0, 1, 1]], 1, 0, 1, 0),
                ([[0, 0, 1], [0, 0, 1], [0, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 1], [0, 0, 1], [0, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 1], [0, 0, 1], [1, 1, 1]], 1, 1, 1, 0),
                ([[0, 0, 1], [0, 0, 1], [1, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 1], [0, 0, 1], [1, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 1], [0, 0, 1], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 0, 1], [0, 0, 2], [0, 0, 2]], 0, 0, 0, 0),
                ([[0, 0, 1], [0, 0, 2], [0, 1, 1]], 0, 0, 0, 0),
                ([[0, 0, 1], [0, 0, 2], [0, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 1], [0, 0, 2], [0, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 1], [0, 0, 2], [1, 1, 1]], 1, 1, 0, 0),
                ([[0, 0, 1], [0, 0, 2], [1, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 1], [0, 0, 2], [1, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 1], [0, 0, 2], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 0, 1], [0, 1, 1], [0, 1, 1]], 1, 0, 1, 0),
                ([[0, 0, 1], [0, 1, 1], [0, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 1], [0, 1, 1], [0, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 1], [0, 1, 1], [1, 1, 1]], 1, 1, 1, 1),
                ([[0, 0, 1], [0, 1, 1], [1, 1, 2]], 1, 0, 0, 1),
                ([[0, 0, 1], [0, 1, 1], [1, 2, 2]], 1, 0, 0, 1),
                ([[0, 0, 1], [0, 1, 1], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 0, 1], [0, 1, 2], [0, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 1], [0, 1, 2], [0, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 1], [0, 1, 2], [1, 1, 1]], 1, 1, 0, 1),
                ([[0, 0, 1], [0, 1, 2], [1, 1, 2]], 1, 0, 0, 1),
                ([[0, 0, 1], [0, 1, 2], [1, 2, 2]], 1, 0, 0, 1),
                ([[0, 0, 1], [0, 1, 2], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 0, 1], [0, 2, 2], [0, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 1], [0, 2, 2], [1, 1, 1]], 1, 1, 0, 0),
                ([[0, 0, 1], [0, 2, 2], [1, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 1], [0, 2, 2], [1, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 1], [0, 2, 2], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 0, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 1, 1),
                ([[0, 0, 1], [1, 1, 1], [1, 1, 2]], 1, 1, 0, 1),
                ([[0, 0, 1], [1, 1, 1], [1, 2, 2]], 1, 1, 0, 1),
                ([[0, 0, 1], [1, 1, 1], [2, 2, 2]], 1, 1, 0, 0),
                ([[0, 0, 1], [1, 1, 2], [1, 1, 2]], 1, 0, 0, 1),
                ([[0, 0, 1], [1, 1, 2], [1, 2, 2]], 1, 0, 0, 1),
                ([[0, 0, 1], [1, 1, 2], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 0, 1], [1, 2, 2], [1, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 1], [1, 2, 2], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 0, 1], [2, 2, 2], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 0, 2], [0, 0, 2], [0, 0, 2]], 2, 0, 2, 0),
                ([[0, 0, 2], [0, 0, 2], [0, 1, 1]], 0, 0, 0, 0),
                ([[0, 0, 2], [0, 0, 2], [0, 1, 2]], 2, 0, 2, 0),
                ([[0, 0, 2], [0, 0, 2], [0, 2, 2]], 2, 0, 2, 0),
                ([[0, 0, 2], [0, 0, 2], [1, 1, 1]], 1, 1, 0, 0),
                ([[0, 0, 2], [0, 0, 2], [1, 1, 2]], 2, 0, 2, 0),
                ([[0, 0, 2], [0, 0, 2], [1, 2, 2]], 2, 0, 2, 0),
                ([[0, 0, 2], [0, 0, 2], [2, 2, 2]], 2, 2, 2, 0),
                ([[0, 0, 2], [0, 1, 1], [0, 1, 1]], 0, 0, 0, 0),
                ([[0, 0, 2], [0, 1, 1], [0, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 2], [0, 1, 1], [0, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 2], [0, 1, 1], [1, 1, 1]], 1, 1, 0, 0),
                ([[0, 0, 2], [0, 1, 1], [1, 1, 2]], 0, 0, 0, 0),
                ([[0, 0, 2], [0, 1, 1], [1, 2, 2]], 0, 0, 0, 0),
                ([[0, 0, 2], [0, 1, 1], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 0, 2], [0, 1, 2], [0, 1, 2]], 2, 0, 2, 0),
                ([[0, 0, 2], [0, 1, 2], [0, 2, 2]], 2, 0, 2, 0),
                ([[0, 0, 2], [0, 1, 2], [1, 1, 1]], 1, 1, 0, 0),
                ([[0, 0, 2], [0, 1, 2], [1, 1, 2]], 2, 0, 2, 0),
                ([[0, 0, 2], [0, 1, 2], [1, 2, 2]], 2, 0, 2, 0),
                ([[0, 0, 2], [0, 1, 2], [2, 2, 2]], 2, 2, 2, 0),
                ([[0, 0, 2], [0, 2, 2], [0, 2, 2]], 2, 0, 2, 0),
                ([[0, 0, 2], [0, 2, 2], [1, 1, 1]], 1, 1, 0, 0),
                ([[0, 0, 2], [0, 2, 2], [1, 1, 2]], 2, 0, 2, 0),
                ([[0, 0, 2], [0, 2, 2], [1, 2, 2]], 2, 0, 2, 0),
                ([[0, 0, 2], [0, 2, 2], [2, 2, 2]], 2, 2, 2, 2),
                ([[0, 0, 2], [1, 1, 1], [1, 1, 1]], 1, 1, 0, 0),
                ([[0, 0, 2], [1, 1, 1], [1, 1, 2]], 1, 1, 0, 0),
                ([[0, 0, 2], [1, 1, 1], [1, 2, 2]], 1, 1, 0, 0),
                ([[0, 0, 2], [1, 1, 1], [2, 2, 2]], 1, 1, 0, 0),
                ([[0, 0, 2], [1, 1, 2], [1, 1, 2]], 2, 0, 2, 0),
                ([[0, 0, 2], [1, 1, 2], [1, 2, 2]], 2, 0, 2, 0),
                ([[0, 0, 2], [1, 1, 2], [2, 2, 2]], 2, 2, 2, 0),
                ([[0, 0, 2], [1, 2, 2], [1, 2, 2]], 2, 0, 2, 0),
                ([[0, 0, 2], [1, 2, 2], [2, 2, 2]], 2, 2, 2, 2),
                ([[0, 0, 2], [2, 2, 2], [2, 2, 2]], 2, 2, 2, 2),
                ([[0, 1, 1], [0, 1, 1], [0, 1, 1]], 1, 0, 1, 0),
                ([[0, 1, 1], [0, 1, 1], [0, 1, 2]], 1, 0, 1, 0),
                ([[0, 1, 1], [0, 1, 1], [0, 2, 2]], 0, 0, 0, 0),
                ([[0, 1, 1], [0, 1, 1], [1, 1, 1]], 1, 1, 1, 1),
                ([[0, 1, 1], [0, 1, 1], [1, 1, 2]], 1, 0, 1, 1),
                ([[0, 1, 1], [0, 1, 1], [1, 2, 2]], 1, 0, 0, 1),
                ([[0, 1, 1], [0, 1, 1], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 1, 1], [0, 1, 2], [0, 1, 2]], 1, 0, 1, 0),
                ([[0, 1, 1], [0, 1, 2], [0, 2, 2]], 0, 0, 0, 0),
                ([[0, 1, 1], [0, 1, 2], [1, 1, 1]], 1, 1, 1, 1),
                ([[0, 1, 1], [0, 1, 2], [1, 1, 2]], 1, 0, 1, 1),
                ([[0, 1, 1], [0, 1, 2], [1, 2, 2]], 1, 0, 0, 1),
                ([[0, 1, 1], [0, 1, 2], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 1, 1], [0, 2, 2], [0, 2, 2]], 0, 0, 0, 0),
                ([[0, 1, 1], [0, 2, 2], [1, 1, 1]], 1, 1, 0, 0),
                ([[0, 1, 1], [0, 2, 2], [1, 1, 2]], 0, 0, 0, 0),
                ([[0, 1, 1], [0, 2, 2], [1, 2, 2]], 0, 0, 0, 0),
                ([[0, 1, 1], [0, 2, 2], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 1, 1),
                ([[0, 1, 1], [1, 1, 1], [1, 1, 2]], 1, 1, 1, 1),
                ([[0, 1, 1], [1, 1, 1], [1, 2, 2]], 1, 1, 0, 1),
                ([[0, 1, 1], [1, 1, 1], [2, 2, 2]], 1, 1, 0, 0),
                ([[0, 1, 1], [1, 1, 2], [1, 1, 2]], 1, 0, 1, 1),
                ([[0, 1, 1], [1, 1, 2], [1, 2, 2]], 1, 0, 0, 1),
                ([[0, 1, 1], [1, 1, 2], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 1, 1], [1, 2, 2], [1, 2, 2]], 0, 0, 0, 0),
                ([[0, 1, 1], [1, 2, 2], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 1, 1], [2, 2, 2], [2, 2, 2]], 2, 2, 0, 0),
                ([[0, 1, 2], [0, 1, 2], [0, 1, 2]], 1, 0, 1, 0),
                ([[0, 1, 2], [0, 1, 2], [0, 2, 2]], 2, 0, 2, 0),
                ([[0, 1, 2], [0, 1, 2], [1, 1, 1]], 1, 1, 1, 0),
                ([[0, 1, 2], [0, 1, 2], [1, 1, 2]], 1, 0, 1, 0),
                ([[0, 1, 2], [0, 1, 2], [1, 2, 2]], 2, 0, 2, 0),
                ([[0, 1, 2], [0, 1, 2], [2, 2, 2]], 2, 2, 2, 0),
                ([[0, 1, 2], [0, 2, 2], [0, 2, 2]], 2, 0, 2, 0),
                ([[0, 1, 2], [0, 2, 2], [1, 1, 1]], 1, 1, 0, 0),
                ([[0, 1, 2], [0, 2, 2], [1, 1, 2]], 2, 0, 2, 0),
                ([[0, 1, 2], [0, 2, 2], [1, 2, 2]], 2, 0, 2, 0),
                ([[0, 1, 2], [0, 2, 2], [2, 2, 2]], 2, 2, 2, 2),
                ([[0, 1, 2], [1, 1, 1], [1, 1, 1]], 1, 1, 1, 0),
                ([[0, 1, 2], [1, 1, 1], [1, 1, 2]], 1, 1, 1, 0),
                ([[0, 1, 2], [1, 1, 1], [1, 2, 2]], 1, 1, 0, 0),
                ([[0, 1, 2], [1, 1, 1], [2, 2, 2]], 1, 1, 0, 0),
                ([[0, 1, 2], [1, 1, 2], [1, 1, 2]], 1, 0, 1, 0),
                ([[0, 1, 2], [1, 1, 2], [1, 2, 2]], 2, 0, 2, 0),
                ([[0, 1, 2], [1, 1, 2], [2, 2, 2]], 2, 2, 2, 0),
                ([[0, 1, 2], [1, 2, 2], [1, 2, 2]], 2, 0, 2, 0),
                ([[0, 1, 2], [1, 2, 2], [2, 2, 2]], 2, 2, 2, 2),
                ([[0, 1, 2], [2, 2, 2], [2, 2, 2]], 2, 2, 2, 2),
                ([[0, 2, 2], [0, 2, 2], [0, 2, 2]], 2, 0, 2, 0),
                ([[0, 2, 2], [0, 2, 2], [1, 1, 1]], 1, 1, 0, 0),
                ([[0, 2, 2], [0, 2, 2], [1, 1, 2]], 2, 0, 2, 0),
                ([[0, 2, 2], [0, 2, 2], [1, 2, 2]], 2, 0, 2, 0),
                ([[0, 2, 2], [0, 2, 2], [2, 2, 2]], 2, 2, 2, 2),
                ([[0, 2, 2], [1, 1, 1], [1, 1, 1]], 1, 1, 0, 0),
                ([[0, 2, 2], [1, 1, 1], [1, 1, 2]], 1, 1, 0, 0),
                ([[0, 2, 2], [1, 1, 1], [1, 2, 2]], 1, 1, 0, 0),
                ([[0, 2, 2], [1, 1, 1], [2, 2, 2]], 1, 1, 0, 0),
                ([[0, 2, 2], [1, 1, 2], [1, 1, 2]], 2, 0, 2, 0),
                ([[0, 2, 2], [1, 1, 2], [1, 2, 2]], 2, 0, 2, 0),
                ([[0, 2, 2], [1, 1, 2], [2, 2, 2]], 2, 2, 2, 0),
                ([[0, 2, 2], [1, 2, 2], [1, 2, 2]], 2, 0, 2, 0),
                ([[0, 2, 2], [1, 2, 2], [2, 2, 2]], 2, 2, 2, 2),
                ([[0, 2, 2], [2, 2, 2], [2, 2, 2]], 2, 2, 2, 2),
                ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 1, 1),
                ([[1, 1, 1], [1, 1, 1], [1, 1, 2]], 1, 1, 1, 1),
                ([[1, 1, 1], [1, 1, 1], [1, 2, 2]], 1, 1, 1, 1),
                ([[1, 1, 1], [1, 1, 1], [2, 2, 2]], 1, 1, 0, 0),
                ([[1, 1, 1], [1, 1, 2], [1, 1, 2]], 1, 1, 1, 1),
                ([[1, 1, 1], [1, 1, 2], [1, 2, 2]], 1, 1, 1, 1),
                ([[1, 1, 1], [1, 1, 2], [2, 2, 2]], 1, 1, 0, 0),
                ([[1, 1, 1], [1, 2, 2], [1, 2, 2]], 1, 1, 1, 0),
                ([[1, 1, 1], [1, 2, 2], [2, 2, 2]], 1, 1, 0, 0),
                ([[1, 1, 1], [2, 2, 2], [2, 2, 2]], 1, 1, 0, 0),
                ([[1, 1, 2], [1, 1, 2], [1, 1, 2]], 1, 0, 1, 0),
                ([[1, 1, 2], [1, 1, 2], [1, 2, 2]], 1, 0, 1, 0),
                ([[1, 1, 2], [1, 1, 2], [2, 2, 2]], 2, 2, 2, 0),
                ([[1, 1, 2], [1, 2, 2], [1, 2, 2]], 1, 0, 1, 0),
                ([[1, 1, 2], [1, 2, 2], [2, 2, 2]], 2, 2, 2, 2),
                ([[1, 1, 2], [2, 2, 2], [2, 2, 2]], 2, 2, 2, 2),
                ([[1, 2, 2], [1, 2, 2], [1, 2, 2]], 1, 0, 1, 0),
                ([[1, 2, 2], [1, 2, 2], [2, 2, 2]], 2, 2, 2, 2),
                ([[1, 2, 2], [2, 2, 2], [2, 2, 2]], 2, 2, 2, 2),
                ([[2, 2, 2], [2, 2, 2], [2, 2, 2]], 2, 2, 2, 2))


def debug_check_board_full_n_in_a_row():
    for info in known_values:
        boardval = tic_tac_toe.check_board_full_n_in_a_row(info[0])
        boardval_horizontal = \
            tic_tac_toe.check_board_horizontally_full(info[0])
        boardval_vertical = tic_tac_toe.check_board_vertically_full(info[0])
        boardval_diagonal = tic_tac_toe.check_board_diagonally_full(info[0])
        expected_boardval = info[1]
        expected_boardval_horizontal = info[2]
        expected_boardval_vertical = info[3]
        expected_boardval_diagonal = info[4]
        if boardval is not expected_boardval:
            print("{0} | boardval: {1}, expected: {2}"
                  .format(info[0], boardval, expected_boardval))
        if boardval_horizontal is not expected_boardval_horizontal:
            print("{0} | boardval_horizontal: {1}, expected: {2}"
                  .format(info[0], boardval_horizontal,
                          expected_boardval_horizontal))
        if boardval_vertical is not expected_boardval_vertical:
            print("{0} | boardval_vertical: {1}, expected: {2}"
                  .format(info[0], boardval_vertical,
                          expected_boardval_vertical))
        if boardval_diagonal is not expected_boardval_diagonal:
            print("{0} | boardval_diagonal: {1}, expected: {2}"
                  .format(info[0], boardval_diagonal,
                          expected_boardval_diagonal))
    return


# format: board_array, expected_num_zeros
count_zeros_variations = (([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 9),
                          ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 0),
                          ([[2, 2, 2], [2, 2, 2], [2, 2, 2]], 0),
                          ([[0, 0, 0], [1, 1, 1], [1, 1, 1]], 3),
                          ([[1, 1, 1], [0, 0, 0], [1, 1, 1]], 3),
                          ([[1, 1, 1], [1, 1, 1], [0, 0, 0]], 3),
                          ([[1, 1, 0], [1, 1, 0], [1, 1, 0]], 3),
                          ([[1, 0, 1], [1, 0, 1], [1, 0, 1]], 3),
                          ([[0, 1, 1], [1, 1, 1], [1, 1, 1]], 1),
                          ([[0, 0, 1], [1, 1, 1], [1, 1, 1]], 2),
                          ([[0, 0, 0], [1, 1, 1], [1, 1, 1]], 3),
                          ([[0, 0, 0], [0, 1, 1], [1, 1, 1]], 4),
                          ([[0, 0, 0], [0, 0, 1], [1, 1, 1]], 5),
                          ([[0, 0, 0], [0, 0, 0], [1, 1, 1]], 6),
                          ([[0, 0, 0], [0, 0, 0], [0, 1, 1]], 7),
                          ([[0, 0, 0], [0, 0, 0], [0, 0, 1]], 8),
                          ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 9))


def debug_count_zeros():
    for info in count_zeros_variations:
        board_array = info[0]
        expected_num_zeros = info[1]
        zeros_counted = tic_tac_toe.count_zeros(board_array)
        if zeros_counted is not expected_num_zeros:
            print("count_zeros: board - {0}, zero count: {1} "
                  "expected zero count: {2}".format(board_array, zeros_counted,
                                                    expected_num_zeros))


def check_for_assertion_error(function, values_to_pass):
    '''checks to see if a given function outpus assertion errors with
    specified arguments

    -- function: the function that is being tested

    -- values_to_pass: a list (a tuple is also acceptable) of values to pass to
                       the function in question'''
    assertion_raised = False
    try:
        function(*values_to_pass)
    except AssertionError:
        assertion_raised = True
    return assertion_raised


def debug_swap_players():
    expected_exception_values = [17, -8, tic_tac_toe.Player.nobody.value]

    for value in expected_exception_values:
        value_list = [value]  # need to pass the value in a list
        assertion_raised = check_for_assertion_error(tic_tac_toe.swap_players,
                                                     value_list)
        if assertion_raised is False:
            print("debug_swap_players: assertion not raised when passing value"
                  " {0}".format(value))

    player1_value = tic_tac_toe.Player.player1.value
    player2_value = tic_tac_toe.Player.player2.value

    if tic_tac_toe.swap_players(player1_value) is not player2_value:
        print("debug_swap_players: swapping player 1 did not produce player2")

    if tic_tac_toe.swap_players(player2_value) is not player1_value:
        print("debug_swap_players: swapping player 2 did not produce player1")


def debug_WhosTurnGenerator():
    # test with player 1 starting
    player_one_starts = True
    player_one_expected_output = [1, 2, 1, 2, 1, 2]
    player_one_first_6 = itertools.islice(
        tic_tac_toe.WhosTurnGenerator(player_one_starts), 0, 6)
    player_one_output = []
    for item in player_one_first_6:
        player_one_output.append(item)

    # test with player 2 starting
    player_two_starts = False
    player_two_expected_output = [2, 1, 2, 1, 2, 1]
    player_two_first_6 = itertools.islice(
        tic_tac_toe.WhosTurnGenerator(player_two_starts), 0, 6)
    player_two_output = []
    for item in player_two_first_6:
        player_two_output.append(item)

    if player_one_output != player_one_expected_output:
        print("WhosTurnGenerator: player_one_output != "
              "player_one_expected_output \n \
              player_one_output: {0} \n \
              player_one_expected_output {1}"
              .format(player_one_output, player_one_expected_output))

    if player_two_output != player_two_expected_output:
        print("WhosTurnGenerator: player_two_output != "
              "player_two_expected_output \n \
              player_two_output: {0} \n \
              player_two_expected_output {1}"
              .format(player_two_output, player_two_expected_output))


def debug_get_diagonals():
    # See expected results for board_4x4 if the diagonal locations/directions
    # are confusing

    #  1 0
    #  0 1
    board_2x2 = (
        [[1, 0], [0, 1]],  # board
        ([[0], [1, 1], [0]],  # down right diaganol
         [[1], [0, 0], [1]])  # down left diagonal
        )
    #  1 2 1
    #  2 1 0
    #  1 0 2
    board_3x3 = (
        [[1, 2, 1], [2, 1, 0], [1, 0, 2]],  # board
        ([[1], [2, 0], [1, 1, 2], [2, 0], [1]],  # down right diaganal
         [[2], [0, 0], [1, 1, 1], [2, 2], [1]])  # down left diagonal
    )
    #  0 1 2 3  v                  v
    #  0 1 2 3   \ down           / down
    #  0 1 2 3    \ right        / left
    #  0 1 2 3     v            v
    board_4x4 = (
        [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]],  # board
        ([[3], [2, 3], [1, 2, 3], [0, 1, 2, 3], [0, 1, 2], [0, 1], [0]],  # dr
         [[3], [3, 2], [3, 2, 1], [3, 2, 1, 0], [2, 1, 0], [1, 0], [0]])  # dl
    )

    boards = (board_2x2[0], board_3x3[0], board_4x4[0])
    expected_tuples = (board_2x2[1], board_3x3[1], board_4x4[1])
    results_tuples = [tic_tac_toe.get_diagonals(board) for board in boards]

    num_boards = 3
    for i in range(num_boards):
        if expected_tuples[i] != results_tuples[i]:
            print("get diagonals: for board:")
            for row in boards[i]:
                print(row)
            print("expected: {0}\n"
                  "got:      {1}".format(expected_tuples[i],
                                         results_tuples[i]))


if __name__ == "__main__":
    debug_node()
    debug_check_board_full_n_in_a_row()
    debug_count_zeros()
    debug_swap_players()
    debug_WhosTurnGenerator()
