def check_board_horizontally(board_array):
    '''check the horizontal rows of a 3x3 gameboard,  returning 0 if no 3 in a
    row is found,  and the player number who has the first three in a row
    otherwise'''
    ret = 0
    # check horizontal rows
    for i in range(3):
        if board_array[i][0] is not 0:
            if board_array[i][0] == board_array[i][1] == board_array[i][2]:
                ret = board_array[i][0]
                break
    return ret


def check_board_vertically(board_array):
    '''check the vertical rows of a 3x3 gameboard,  returning 0 if no 3 in a
    row is found,  and the player number who has the first three in a row
    otherwise'''
    ret = 0
    # check vertical rows
    for i in range(3):
        if board_array[0][i] is not 0:
            if board_array[0][i] == board_array[1][i] == board_array[2][i]:
                ret = board_array[0][i]
                break
    return ret


def check_board_diagonally(board_array):
    '''check the diagonal cross section of a 3x3 gameboard,  returning 0 if no 3
    in a row is found,  and the player number who has the first three in a row
    otherwise'''
    ret = 0
    if board_array[1][1] is not 0:
        if board_array[0][0] == board_array[1][1] == board_array[2][2]:
            ret = board_array[1][1]
        if board_array[0][2] == board_array[1][1] == board_array[2][0]:
            ret = board_array[1][1]
    return ret


def check_board(board_array):
    '''Check a 3x3 tictactoe board for 3 in a row
    Arguments: board_array - a 3x3 array representing a tic tac to board,  it
               is assumed that 0 spaces are unocupied,  and numbered spaces are
               occupied by a player represented by that number
    Returns: 0 if no three_in_a_row found,  otherwise the number of the player
             with the (first) three_in_a_row found'''
    ret = 0
    if ret == 0:
        ret = check_board_horizontally(board_array)
    if ret == 0:
        ret = check_board_diagonally(board_array)
    if ret == 0:
        ret = check_board_vertically(board_array)
    return ret


def debug_check_board():
    boardvalhorizontal = 0
    boardvalvertical = 0
    boardvaldiagonal = 0
    boardvalnone = 0
    boardhorizontal = [[1, 1, 1], [2, 1, 2], [1, 2, 1]]
    boardvertical = [[0, 2, 0], [1, 2, 2], [1, 2, 1]]
    boarddiagonal = [[1, 2, 1], [2, 1, 2], [1, 2, 1]]
    boardnone = [[0, 0, 0], [2, 1, 2], [1, 2, 1]]
    boardvalhorizontal = check_board(boardhorizontal)
    boardvalvertical = check_board(boardvertical)
    boardvaldiagonal = check_board(boarddiagonal)
    boardvalnone = check_board(boardnone)
    print("boardvalnone: {0}, boardvalhorizontal: {1}, boardvalvertical: {2}, \
          boardvaldiagonal: {3}".format(boardvalnone, boardvalhorizontal,
                                        boardvalvertical, boardvaldiagonal))
    return


class Node:
    '''A node in our list-tree'''
    def __init__(self, parent, board_array, computer_value):
        self.child_wins = 0
        self.winner = check_board(board_array)
        self.parent = parent

        if self.parent is not None:
            if self.winner == computer_value:
                self.parent.child_wins += 1

        self.children = []
        self.board_array = board_array

    def add_child(self, child):
        self.children.append(child)

    def find_child(self, board_array):
        for child in self.children:
            if child.board_array == board_array:
                return child
        return None


def debug_node():
    board_array = [[0 for x in range(3)] for x in range(3)]
    parent = Node(None, board_array, 1)
    children_arrays = []
    for i in range(3):
        for j in range(3):
            new_board = [[0 for x in range(3)] for x in range(3)]
            new_board[i][j] = 1
            children_arrays.append(new_board)
    for child_array in children_arrays:
        child_node = Node(parent, child_array, 1)
        parent.add_child(child_node)

    print(parent.children)
    for child in parent.children:
        print(child.board_array)
        print(child.winner)
    print(parent.board_array)
    print(parent.winner)


if __name__ == '__main__':
    debug_check_board()
    debug_node()
