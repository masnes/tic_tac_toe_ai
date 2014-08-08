import copy


def check_board_horizontally(board_array):
    '''check the horizontal rows of a nxn gameboard, returning 0 if no
    n-in-a-row is found, and the player number who has the first n-in-a-row
    otherwise

    -- board_array: an nxn array carrying the current board state'''
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
    otherwise

    -- board_array: an nxn array carrying the current board state'''
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


# TODO: check boards in true n_in_a_row style
def check_board_diagonally(board_array, n_in_a_row=3):
    '''check the diagonal cross section of a nxn gameboard,  returning 0 if no
    n-in-a-row is found, and the player number who has the first n-in-a-row
    otherwise

    -- board_array: an nxn array carrying the current board state
    -- n_in_a_row: how many items in a row constitutes a win'''
    num_subarrays = len(board_array)
    num_items_in_subarray = len(board_array[0])
    assert num_subarrays == num_items_in_subarray, "Array is not nxn"

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


def check_board(board_array, n_in_a_row=3):
    '''Check a 3x3 tictactoe board for 3 in a row

    -- board_array:  a nxn array representing a tic tac to board,  it
                     is assumed that 0 spaces are unocupied,  and numbered
                     spaces are occupied by a player represented by that number

    -- n_in_a_row: how many items in a row constitutes a win

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


# Note: this function not currently in use
def count_zeros(board_array):
    '''Counts number of zeros in an nxn array

    -- board_array: an nxn array'''
    zero_count = 0
    for row in board_array:
        for item in row:
            zero_count += (item == 0)
    return zero_count


class WhosTurnGenerator:
    '''Iterator that alternates turns between player 1 and player 2

    -- does_player_one_start: Bool, option to initiate the generator
    with player one, or alternately player two, starting'''

    def __init__(self, does_player_one_start=True):
        if does_player_one_start:
            self.starting_player = 1
        else:
            self.starting_player = 2

    def __iter__(self):
        self.player = self.starting_player
        return self

    def __next__(self):
        self.player = 1 + (self.player == 1)
        return self.player
        # There's no StopIteration by design


def gen_play_permutations(board_array, does_player_one_start=True):
    '''Gens each possible move left in the board for a given player
    Note: there's no 3-in-a-row checking here. That must be done elsewhere

    -- board_array: an nxn array holding the current state of play
    -- players_turn: indicates which players turn it is to play'''
    # initialize generator to flip player turns
    turn_gen = WhosTurnGenerator(does_player_one_start)
    turn_gen.__iter__()
    # deepcopy, so we don't change what we're iterating over
    board_to_ret = copy.deepcopy(board_array)
    # get starting players turn
    players_turn = turn_gen.player
    for i, row in enumerate(board_array):
        for j, square in enumerate(row):
            if square == 0:
                # player a goes
                board_to_ret[i][j] = players_turn
                yield board_to_ret
                # player b goes
                players_turn = turn_gen.__next__()
                board_to_ret[i][j] = players_turn
                yield board_to_ret
                # reset state for the next square/row
                players_turn = turn_gen.__next__()
                board_to_ret[i][j] = 0
    raise StopIteration


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

        self.children = []
        self.board_array = board_array

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def has_child(self, board_array):
        for child in self.children:
            if child.board_array == board_array:
                return child
        return None


def add_node_to_tree(board_array, parent_node):
    '''Adds a node to the current tree. If the parent_node is not there, adds a
    parent node. Otherwise adds the node as a child of the parent node

    -- board_array: the nxn board state for the node to be added
    -- parent_node: the nodes parent, if any'''
    if parent_node is None:
        parent_node = Node(None, board_array)
        new_child = parent_node
    else:
        child_node = Node(parent_node, board_array)
        parent_node.add_child(child_node)
        new_child = child_node
    return new_child


def build_new_board_array(dimensions):
    '''Builds a board_array (list of lists of ints) of dimensions nxn,
    initialize to all 0's

    -- dimensions: the size of n for our nxn board_array'''
    sub_array = []
    board_array = []
    for i in range(dimensions):
        sub_array.append(0)
    for j in range(dimensions):
        board_array.append(sub_array)
    return board_array


if __name__ == '__main__':
    # some throwaway code to keep pylint happy
    check_board([[1, 1, 1], [2, 2, 2], [0, 1, 0]])
    Node(None,  [[1, 1, 1], [2, 2, 2], [0, 1, 0]])
    for board in gen_play_permutations([[1, 1, 1], [2, 2, 2], [0, 1, 0]]):
        print(board)
    else:  # really should be "then:"
        print("done")
