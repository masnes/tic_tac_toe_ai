import queue


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


# Note: this function is not currently in use, but is very useful for debugging
def count_zeros(board_array):
    '''Counts number of zeros in an nxn array

    -- board_array: an nxn array'''
    zero_count = 0
    for row in board_array:
        for item in row:
            zero_count += (item == 0)
    return zero_count


def swap_players(player):
    if player == 2:
        return 1
    else:
        return 2


class WhosTurnGenerator():
    '''Alternates turns between player 1 and player 2

    -- player_one_starts: Bool, option to initiate the generator
    with either player one, or player 2 starting'''
    def __init__(self, player_one_starts=True):
        if player_one_starts:
            self.starting_player = 1
        else:
            self.starting_player = 2

    def __iter__(self):
        if self.starting_player == 2:
            self.current_player = 1
        else:
            self.current_player = 2
        return self

    def __next__(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1
        return self.current_player


def copy_list_of_lists(board_array):
    '''Given a list of lists (a board_array), produce a copy of all items within
    that list and return the copy. Useful for avoiding python pass-by-reference
    issues

    -- board_array: an nxn array holding the current state of play'''
    new_board_array = []
    for row in board_array:
        new_row = list(row)
        new_board_array.append(new_row)
    return new_board_array


def gen_play_permutations(board_array, players_turn):
    '''Gens each possible move left in the board for a given player

    -- board_array: an nxn array holding the current state of play
    -- players_turn: indicates which players turn it is to play'''
    for i, row in enumerate(board_array):
        for j, square in enumerate(row):
            if square == 0:
                new_board_array = copy_list_of_lists(board_array)
                new_board_array[i][j] = players_turn
                yield new_board_array
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


def get_new_depth(max_depth):
    '''reduce max_depth by one if max_depth is a number. If max_depth is None, keep
    it as None

    max_depth -- a measure of how many more recursions are allowed. Once this
    reaches 0 recursion stops. If None, infinite recursions are allowed (the
    recursion must be stopped by a non-depth-related base case)'''
    if max_depth is not None:
        new_depth = max_depth - 1
    else:
        new_depth = None
    return new_depth


def add_nodes_recursively(parent_node, player_turn, max_depth):
    # recursive base cases
    if parent_node.winner:
        return
    if max_depth == 0:
        return

    # build children
    for board_variation in gen_play_permutations(parent_node.board_array,
                                                 player_turn):
        child = Node(parent_node, board_variation)
        parent_node.add_child(child)

    # change state before continuing recursion
    next_player = swap_players(player_turn)
    new_depth = get_new_depth(max_depth)

    # recurse for all children
    for child in parent_node.children:
        add_nodes_recursively(child, next_player, new_depth)


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


def build_decision_tree(computer_goes_first=True, board_dimensions=3,
                        max_depth=None):
    '''Builds a decision tree for a board of given dimensions
    up to a maximum depth, or until all possibilities are exhausted

    -- board_dimensions: how big a board to calculate for, base is 3, the
    generic tic tac toe size

    -- depth: How deep a decision tree to build. Pass 0 or None for a full
    tree.

    Returns: root node of tree'''
    board_array = build_new_board_array(board_dimensions)

    if computer_goes_first:
        computer_player = 1
    else:
        computer_player = 2

    root = Node(None, board_array, computer_player)
    for n in gen_play_permutations(board_array):
        # new_node = Node(root,
        pass


if __name__ == '__main__':
    # some throwaway code to keep pylint happy
    check_board([[1, 1, 1], [2, 2, 2], [0, 1, 0]])
    Node(None,  [[1, 1, 1], [2, 2, 2], [0, 1, 0]])
    for board in gen_play_permutations([[1, 1, 1], [2, 2, 2], [0, 1, 0]], 1):
        print(board)
    else:  # really should be "then:"
        print("done with gen_play_permutations")

    for i in range(5):
        new_board = build_new_board_array(i)
        print(new_board)
def print_tree_structure(root):
    fifo = queue.Queue()
    fifo.put(root)
    next_item = fifo.get()
    while next_item:
        num_children = len(next_item.children)
        print(next_item.children)
        print(num_children)
        for child in next_item.children:
            fifo.put(child)
        next_item = fifo.get()
