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


class KnownBoardValues:
    # format: board, check, horizontal_check, vertical_check, diagonal_check
    (([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0, 0, 0, 0))


def debug_check_board():
    boardvalhorizontal = 0
    boardvalvertical = 0
    boardvaldiagonal = 0
    boardvalnone = 0
    boardhorizontal = [[1, 1, 1], [2, 1, 2], [1, 2, 1]]
    boardvertical = [[0, 2, 0], [1, 2, 2], [1, 2, 1]]
    boarddiagonal = [[1, 2, 1], [2, 1, 2], [1, 2, 1]]
    boardnone = [[0, 0, 0], [2, 1, 2], [1, 2, 1]]
    boardvalhorizontal = tic_tac_toe.check_board(boardhorizontal)
    boardvalvertical = tic_tac_toe.check_board(boardvertical)
    boardvaldiagonal = tic_tac_toe.check_board(boarddiagonal)
    boardvalnone = tic_tac_toe.check_board(boardnone)
    print("boardvalnone = {0}, expected")
    print("boardvalnone: {0}, boardvalhorizontal: {1}, boardvalvertical: {2}, \
          boardvaldiagonal: {3}".format(boardvalnone, boardvalhorizontal,
                                        boardvalvertical, boardvaldiagonal))
    return

if __name__ == "__main__":
    debug_node()
    debug_check_board()
