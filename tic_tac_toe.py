import cProfile
import queue
from enum import Enum


class Player(Enum):
    '''defining the different possible values for board spaces'''
    # note: keep the values as a count from 0! This allows this class to
    # act as a hash in addition to other enumeration functions.
    # This behavior is expected in function: note_potential_n_in_a_row
    nobody = 0
    player1 = 1
    player2 = 2
    both = 3


def check_board_horizontally_full(board_array):
    '''check the horizontal rows of a nxn gameboard, returning 0 if no
    n-in-a-row is found, and the player number who has the first n-in-a-row
    otherwise

    -- board_array: an nxn array carrying the current board state -- guaranteed
    by check_board function'''
    # check horizontal rows
    ret = 0
    for horizontal_row in board_array:
        items = set(horizontal_row)
        if len(items) == 1:
            ret = items.pop()
            if ret != Player.nobody.value:
                break
    return ret


def check_board_vertically_full(board_array):
    '''check the vertical rows of a nxn gameboard, returning 0 if no
    n-in-a-row is found, and the player number who has the first n-in-a-row
    otherwise

    -- board_array: an nxn array carrying the current board state -- guaranteed
    by check_board function'''
    # check vertical rows
    ret = 0
    # note that vertical_row is a tuple, while in check_board_horizontally
    # it's a list. This doesn't affect the (current) implemenation
    for vertical_row in zip(*board_array):
        items = set(vertical_row)
        if len(items) == 1:
            ret = items.pop()
            if ret != Player.nobody.value:
                break
    return ret


# DONE: check boards in true n_in_a_row style
def check_board_diagonally_full(board_array):
    '''check the diagonal cross section of a nxn gameboard,  returning 0 if no
    n-in-a-row is found, and the player number who has the first n-in-a-row
    otherwise

    -- board_array: an nxn array carrying the current board state -- guaranteed
    by check_board function
    -- n_in_a_row: how many items in a row constitutes a win'''
    ret = Player.nobody.value
    length = len(board_array[0])

    down_right_diagonal_contains_a_player = (board_array[0][0] !=
                                             Player.nobody.value)
    up_right_diagonal_contains_a_player = (board_array[0][length-1] !=
                                           Player.nobody.value)

    # check for n_in_a_row in down right diagonal
    if down_right_diagonal_contains_a_player:
        down_right_diagonal_set = {board_array[i][i] for i in range(0, length)}
        down_right_diagonal_is_n_in_a_row = (len(down_right_diagonal_set) == 1)
    else:
        down_right_diagonal_is_n_in_a_row = False
    # check for n_in_a_row in up right diagonal
    if up_right_diagonal_contains_a_player:
        up_right_diagonal_set = \
            {board_array[i][length-i-1] for i in range(0, length)}
        up_right_diagonal_is_n_in_a_row = (len(up_right_diagonal_set) == 1)
    else:
        up_right_diagonal_is_n_in_a_row = False

    # note an n_in_a_row, and the identity of winning player if found
    # warning: in any (unexpected) cases where both players make an n_in_a_row,
    # only one player's n_in_a_row will be detected
    if down_right_diagonal_is_n_in_a_row:
        ret = down_right_diagonal_set.pop()
    elif up_right_diagonal_is_n_in_a_row:
        ret = up_right_diagonal_set.pop()

    return ret


def check_board_full_n_in_a_row(board_array):
    '''Check a nxn tictactoe board for n in a row

    -- board_array:  a nxn array representing a tic tac to board,  it
                     is assumed that 0 spaces are unocupied,  and numbered
                     spaces are occupied by a player represented by that number

    -- n_in_a_row: how many items in a row constitutes a win

    Returns: 0 if no three_in_a_row found,  otherwise the number of the player
             with the (first) three_in_a_row found'''
    num_subarrays = len(board_array)
    for horizontal_row in board_array:
        num_items_in_subarray = len(horizontal_row)
        assert num_subarrays == num_items_in_subarray, "Array is not nxn"

    ret = Player.nobody.value
    if ret == Player.nobody.value:
        ret = check_board_horizontally_full(board_array)
    if ret == Player.nobody.value:
        ret = check_board_diagonally_full(board_array)
    if ret == Player.nobody.value:
        ret = check_board_vertically_full(board_array)
    return ret


def check_for_almost_n_in_a_row(values_sequence, n_in_a_row):
    '''Takes a list of values of size n_in_a_row. Then checks that list
    for a scenario where all but one of the values represent one player,
    and the final value represents unplayed. In other words, checks for a
    situation where one additional play would win the game

    -- values_sequence: A list of values representing a partial slice of a
    board row, column, or diagonal. Must be the same length as n_in_a_row

    -- n_in_a_row: How many consecutive values constitutes an n_in_a_row

    Returns tuple of:
        (player who has an almost n_in_a_row for this list,
         offset from the beginning of the list where the n_in_a_row occurs)'''
    assert len(values_sequence) == n_in_a_row, \
        "values sequence not the same length as an expected n-in-a-row"
    # counters
    unplayed_count = 0
    player1_count = 0
    player2_count = 0
    # how far from the start of the list the first unplayed square is
    unplayed_offset = 0

    # count occurences
    for offset, value in enumerate(values_sequence):
        if value == Player.player1.value:
            player1_count += 1
        elif value == Player.player2.value:
            player2_count += 1
        elif value == Player.nobody.value:
            unplayed_offset = offset
            unplayed_count += 1

    # check for almost_n_in_a_row
    if unplayed_count == 1:
        if player1_count == n_in_a_row - 1:
            return Player.player1.value, unplayed_offset
        elif player2_count == n_in_a_row - 1:
            return Player.player2.value, unplayed_offset

    # if no almost_n_in_a_row found
    return None, None


def make_list(board_array, starting_i, starting_j, delta_i, delta_j,
              max_length):
    '''given a board_array, a position on that board array, a direction to
    travel from that position, and a number of values to try for: make a list
    of that size, by moving in that direction over the board

    -- board_array: an nxn array carrying the current board state
    -- starting_i: starting row position on the board
    -- starting_j: starting column position on the board
    -- delta_i: rate and direction that we move over rows in the board
    -- delta_j: rate and direction that we move over columns in the board
    -- max_length: max length of the list that we make'''

    new_list = []
    # get parameters needed to move over array and record values
    possible_i_movement = abs((max_length-1) * delta_i)
    possible_j_movement = abs((max_length-1) * delta_j)
    i_max = min(len(board_array) - 1, starting_i + possible_i_movement)
    j_max = min(len(board_array) - 1, starting_j + possible_j_movement)
    i_min = max(0, starting_i - possible_i_movement)
    j_min = max(0, starting_j - possible_j_movement)

    # move over the array, recording the values found
    i = starting_i
    j = starting_j
    while i_min <= i <= i_max and j_min <= j <= j_max:
        new_list.append(board_array[i][j])
        i += delta_i
        j += delta_j
    return new_list


def note_potential_n_in_a_row(n_in_a_row_position_array, player, i, j):
    '''Call this function if a potential n_in_a_row is found (n-1 squares lined
    up horizontally, vertically, or diagonally, with the final square empty).
    It notes the location of the n_in_a_row, and the player who can
    make an n_in_a_row there in a provided n_in_a_row_position_array. If
    another n_in_a_row has been found already in the same position, this
    function will update the state of n_in_a_row_position_array to record that
    both players can make an n_in_a_row by playing there

    -- n_in_a_row_position_array: a board_array sized array used for noting
       where n_in_a_row's could potentially be produced next turn, and who they
       could be produced by

    -- player: the player who can potentially create an n_in_a_row
    -- i: row at which n_in_a_row could be produced
    -- j: column at which n_in_a_row could be produced'''

    assert player == Player(player).value,\
        "Unrecognized player given to n_in_a_row_position_array"
    assert player != Player.nobody.value, \
        "Noting that nobody is making a potential n_in_a_row is useless"

    current = n_in_a_row_position_array[i][j]
    currently_nobody_wins_at_this_position = (current == Player.nobody.value)
    currently_player1_wins_at_this_position = (current == Player.player1.value)
    currently_player2_wins_at_this_position = (current == Player.player2.value)
    a_new_player_wins_at_this_position = (current != player)

    if currently_nobody_wins_at_this_position:
        n_in_a_row_position_array[i][j] = player
    elif (currently_player1_wins_at_this_position or
            currently_player2_wins_at_this_position):
        if a_new_player_wins_at_this_position:
            n_in_a_row_position_array[i][j] = Player.both.value
    return


def check_diagonals_partially(board_array, n_in_a_row_position_array,
                              n_in_a_row):
    '''for an nxn array, find all the diagonals moving from the top left
    of the array to the bottom right. Alter a second inputted array to note the
    positions of these diagonals

    -- board_array: an nxn array (list of lists)

    Returns: tuple (down_right_diagonals, up_right_diagonals)'''

    # Note: the module numpy can also be used to get diagonals. As an exercise
    # for myself, however, I wanted to write this function from scratch
    #
    # a diagram of a tic tac toe board is most helpful for understanding the
    # diagonal traversing part of this function (by far the most complex part).
    # The following applies for any board size, but is best illustrated by a
    # 3x3 board:
    #
    #    0  1  2 (j)
    #  0__|__|__
    #  1__|__|__
    #  2  |  |
    # (i)
    #
    # Note that we have 5 diagonals going each direction (count them),
    # for a board size of nxn, there's (n*2)-1 diagonals
    # we can think of the first 3 (n) diagonals as starting at locations
    # a[0][?]
    #
    # let #'s represent diagonals
    # let s# stand for the start of diagonal #
    #
    # direction
    # v       starting column is not determinate
    #  \       v  v  v
    #   \     s3|s2|s1 <- starting row is determinate
    #    \    __|_3|_2
    #     v     |  | 3
    #
    # and the rest starting at a[0][?]
    #
    #   starting column is determinate
    #   v
    #  __|__|__
    #  s4|__|__ < starting row
    #  s5| 4|   < is not
    #
    # given a starting row, and column position starting_i, starting_j,
    # we can get the rest of the diagonal by incrementing i, j from
    # starting_i, starting_j to the end of the board
    #
    # the diagonals moving the other direction are similar, but not exactly the
    # same. We need to rotate the above diagram, and then move in the other
    # direction:
    #
    #    0  1  3 (j)      v
    #  0 s5|s4|s3        /
    #    --+--+--       /  new
    #  1  4| 3|s2      /   direction
    #    --+--+--     /
    #  2  3| 2|s1    v
    # (i)

    length = len(board_array)
    num_diagonals_per_direction = len(board_array) * 2 - 1

    down_right_diagonals = []
    for n in range(num_diagonals_per_direction):
        # first ceiling(half) diagonals start at a[?][0]
        # second floor(half) diagonals start at a[0][?]
        sub_list = []
        starting_i = max(n-length+1, 0)
        starting_j = max(0, length-n-1)
        i = starting_i
        j = starting_j
        while i < length and j < length:
            sub_list.append(board_array[i][j])
            i += 1
            j += 1
        down_right_diagonals.append(sub_list)

    down_left_diagonals = []
    for n in range(num_diagonals_per_direction):
        # first ceiling(half) diagonals start at a[?][length-1]
        # second floor(half) diagonals start at a[0][?]
        sub_list = []
        starting_i = max(length-n-1, 0)
        starting_j = min(length-1, num_diagonals_per_direction - n - 1)
        i = starting_i
        j = starting_j
        while i < length and j >= 0:
            sub_list.append(board_array[i][j])
            i += 1
            j -= 1
        down_left_diagonals.append(sub_list)

    return (down_right_diagonals, down_left_diagonals)


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
    '''swaps between player 1 and player 2

    -- player: Which player just played (int of either 1 or 2)'''
    assert player == Player.player1.value or player == Player.player2.value, \
        "passed invalid player to swap_players"
    if player == Player.player2.value:
        return Player.player1.value
    elif player == Player.player1.value:
        return Player.player2.value


class WhosTurnGenerator():
    '''Alternates turns between player 1 and player 2

    -- player_one_starts: Bool, option to initiate the generator
    with either player one, or player 2 starting'''
    def __init__(self, player_one_starts=True):
        if player_one_starts:
            self.starting_player = Player.player1.value
        else:
            self.starting_player = Player.player2.value

    def __iter__(self):
        '''Initialize the starting player to the wrong value, so that when
        __next__ is called for the first time, the value returned is correct'''
        self.current_player = swap_players(self.starting_player)
        return self

    def __next__(self):
        self.current_player = swap_players(self.current_player)
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
            if square == Player.nobody.value:
                new_board_array = copy_list_of_lists(board_array)
                new_board_array[i][j] = players_turn
                yield new_board_array
    raise StopIteration


class Node:
    '''A node in our list-tree. The node stores information on what its parent
    is, what its children are, whether it's a winner, and how many winning
    children it has (0 initially, since it starts with no children)'''
    def __init__(self, parent, board_array, computer_value=1):
        '''initialize a node in the list tree

        -- parent: parent node, if any
        -- board_array: a nxn 2d list with the tic-tac-toe state for this node
        -- computer_value: the value that represents the computer on
        board_array, defaults to 1'''
        self.child_computer_wins = 0
        self.child_human_wins = 0
        self.winner = check_board_full_n_in_a_row(board_array)
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


def add_nodes_recursively(parent_node, player_turn, computer_player,
                          max_depth):
    '''given a node with a starting board, continuously play out all possible
    tic tac toe games until a player wins. returns the sum of the number of
    wins in all recursions deeper than and within the current recursion

    -- parent_node: the parent node. Children will be linked with this parent
    -- player_turn: Which player's turn it is to play next
    -- max_depth: how many more levels of recursion are allowed. Infinite if
    None'''
    # insure correct parameters
    assert player_turn == Player.player1.value or player_turn == \
        Player.player2.value
    assert computer_player == Player.player1.value or computer_player == \
        Player.player2.value

    # recursive base cases
    if parent_node.winner:
        return
    if max_depth == 0:
        return

    # build children and sum wins of children
    for board_variation in gen_play_permutations(parent_node.board_array,
                                                 player_turn):
        # build children
        child = Node(parent_node, board_variation)
        parent_node.add_child(child)

    # change state before continuing recursion
    next_player = swap_players(player_turn)
    new_depth = get_new_depth(max_depth)

    # recurse for all children
    for child in parent_node.children:
        add_nodes_recursively(child, next_player, computer_player, new_depth)

        # sum wins of children
        parent_node.child_human_wins += child.child_human_wins
        parent_node.child_computer_wins += child.child_computer_wins
        human_player = swap_players(computer_player)
        if child.winner == computer_player:
            parent_node.child_computer_wins += 1
        elif child.winner == human_player:
            parent_node.child_human_wins += 1


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

    -- depth: How deep a decision tree to build. Pass None for a full
    tree.

    Returns: root node of tree'''
    board_array = build_new_board_array(board_dimensions)

    if computer_goes_first:
        computer_player = Player.player1.value
    else:
        computer_player = Player.player2.value

    root = Node(None, board_array, computer_player)
    starting_player = Player.player1.value
    add_nodes_recursively(root, starting_player, computer_player, max_depth)

    return root


def print_tree_structure(root):
    '''Prints current tree structure. For debugging purposes

    root -- the root node for the tree (or whatever node is to be treated as
    such)'''
    fifo = queue.Queue()
    fifo.put(root)
    next_item = fifo.get()
    while next_item:
        num_children = len(next_item.children)
        print(num_children)
        if num_children:
            for child in next_item.children:
                fifo.put(child)
        if not fifo.empty():
            next_item = fifo.get()
        else:
            next_item = None


def test_queue():
    fifo = queue.Queue()
    fifo.put(5)
    next_item = fifo.get()
    print(next_item)
    fifo.put(3)
    fifo.put(7)
    next_item = fifo.get()
    print(next_item)
    next_item = fifo.get()
    print(next_item)
    if not queue.Empty():
        next_item = fifo.get()
        print(next_item)
    if not queue.Empty():
        next_item = fifo.get()
        print(next_item)
    print("should be: 5, 3, 7, nothing, nothing")


if __name__ == '__main__':
    # board1 = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]
    # some throwaway code to keep pylint happy
    # check_board([[1, 1, 1], [2, 2, 2], [0, 1, 0]])
    #     print(board)
    for board in gen_play_permutations([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 2):
        print(board)
    # else:  # really should be "then:"
    cProfile.run('root = build_decision_tree(True, 3, None)')
    # for child in root.children:
    #     print("board: {0}, computer wins: {1}, player wins: {2}"
    #           .format(child.board_array, child.child_computer_wins,
    #                   child.child_human_wins))
    # print_tree_structure(root)
