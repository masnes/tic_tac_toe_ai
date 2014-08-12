import tic_tac_toe


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


def debug_check_board():
    for info in known_values:
        boardval = tic_tac_toe.check_board(info[0])
        boardval_horizontal = tic_tac_toe.check_board_horizontally(info[0])
        boardval_vertical = tic_tac_toe.check_board_vertically(info[0])
        boardval_diagonal = tic_tac_toe.check_board_diagonally(info[0])
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
            print("count_zeros: board - {0}, zero count: {1}"
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


if __name__ == "__main__":
    debug_node()
    debug_check_board()
    debug_count_zeros()
    debug_swap_players()
