def check_board_horizontally(board_array):
    '''check the horizontal rows of a nxn gameboard, returning 0 if no
    n-in-a-row is found, and the player number who has the first n-in-a-row
    otherwise'''
    # check horizontal rows
    ret = 0
    for horizontal_row in board_array:
        if horizontal_row[0] is not 0:
            items = set(horizontal_row)
            if len(items) == 1:
                ret = items.pop()
                break
    return ret


def check_board_vertically(board_array):
    '''check the vertical rows of a nxn gameboard, returning 0 if no
    n-in-a-row is found, and the player number who has the first n-in-a-row
    otherwise'''
    # check vertical rows
    ret = 0
    # note that vertical_row is a tuple, while in check_board_horizontally
    # it's a list. This doesn't affect the (current) implemenation
    for vertical_row in zip(*board_array):
        if vertical_row[0] is not 0:
            items = set(vertical_row)
            if len(items) == 1:
                ret = items.pop()
                break
    return ret


def check_board_diagonally(board_array):
    '''check the diagonal cross section of a nxn gameboard,  returning 0 if no
    n-in-a-row is found, and the player number who has the first n-in-a-row
    otherwise'''
    ret = 0
    if board_array[1][1]:  # if there's no center, there's no diagonals
        l = len(board_array[0])
        down_right_diagonal = {board_array[i][i] for i in range(0, l)}
        up_right_diagonal = {board_array[i][l-i-1] for i in range(0, l)}
        if len(down_right_diagonal) == 1:
            ret = down_right_diagonal.pop()
        # this part breaks if the "if board_array[1][1]" part is removed
        elif len(up_right_diagonal) == 1:
            ret = up_right_diagonal.pop()
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


def count_zeros(board_array):
    '''Counts number of zeros in an nxn array

    -- board_array: an nxn array'''
    zero_count = 0
    for row in board_array:
        for item in row:
            zero_count += (item == 0)
    return zero_count


def whos_turn_generator(player_one_starts=True):
    '''Alternates turns between player 1 and player 2

    -- player_one_starts: Bool, option to initiate the generator
    with either player one, or player 2 starting'''
    if not player_one_starts:
        current_player = 2
        yield current_player
    while True:
        current_player = 1
        yield current_player
        current_player = 2
        yield current_player


def gen_play_permutations(board_array, players_turn):
    '''Gens each possible move left in the board for a given player

    -- board_array: an nxn array holding the current state of play
    -- players_turn: indicates which players turn it is to play'''
    for i, row in board_array:
        for j, square in row:
            if square == 0:
                board_array[i][j] = players_turn
                yield board_array
                board_array[i][j] = 0
    yield StopIteration


class Node:
    '''A node in our list-tree. The node stores information on what it's parent
    is, what it's children are, whether it's a winner, and how many winning
    children it has'''
    def __init__(self, parent, board_array, computer_value=1):
        '''initialize a node in the list tree

        parameters
        parent -- parent node, if any
        board_array -- a 3x3 2d list with the tic-tac-toe state for this node
        computer_value -- the value that represents the computer on
        board_array, defaults to 1
        '''
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

    def has_child(self, board_array):
        for child in self.children:
            if child.board_array == board_array:
                return child
        return None


if __name__ == '__main__':
    # some throwaway code to keep pylint happy
    check_board([[1, 1, 1], [2, 2, 2], [0, 1, 0]])
    Node(None,  [[1, 1, 1], [2, 2, 2], [0, 1, 0]])
