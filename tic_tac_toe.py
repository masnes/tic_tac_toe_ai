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


def check_board_horizontally_full(board_matrix):
    '''check the horizontal rows of a nxn gameboard, returning 0 if no
    n-in-a-row is found, and the player number who has the first n-in-a-row
    otherwise

    -- board_matrix: an nxn matrix carrying the current board state --
    guaranteed by check_board function'''
    # check horizontal rows
    ret = 0
    for horizontal_row in board_matrix:
        items = set(horizontal_row)
        if len(items) == 1:
            ret = items.pop()
            if ret != Player.nobody.value:
                break
    return ret


def check_board_vertically_full(board_matrix):
    '''check the vertical rows of a nxn gameboard, returning 0 if no
    n-in-a-row is found, and the player number who has the first n-in-a-row
    otherwise

    -- board_matrix: an nxn matrix carrying the current board state --
    guaranteed by check_board function'''
    # check vertical rows
    ret = 0
    # note that vertical_row is a tuple, while in check_board_horizontally
    # it's a list. This doesn't affect the (current) implemenation
    for vertical_row in zip(*board_matrix):
        items = set(vertical_row)
        if len(items) == 1:
            ret = items.pop()
            if ret != Player.nobody.value:
                break
    return ret


# DONE: check boards in true n_in_a_row style
def check_board_diagonally_full(board_matrix):
    '''check the diagonal cross section of a nxn gameboard,  returning 0 if no
    n-in-a-row is found, and the player number who has the first n-in-a-row
    otherwise

    -- board_matrix: an nxn matrix carrying the current board state --
    guaranteed by check_board function
    -- n_in_a_row: how many items in a row constitutes a win'''
    ret = Player.nobody.value
    length = len(board_matrix[0])

    down_right_diagonal_contains_a_player = (board_matrix[0][0] !=
                                             Player.nobody.value)
    up_right_diagonal_contains_a_player = (board_matrix[0][length-1] !=
                                           Player.nobody.value)

    # check for n_in_a_row in down right diagonal
    if down_right_diagonal_contains_a_player:
        down_right_diagonal_set = {board_matrix[i][i] for i in range(length)}
        down_right_diagonal_is_n_in_a_row = (len(down_right_diagonal_set) == 1)
    else:
        down_right_diagonal_is_n_in_a_row = False
    # check for n_in_a_row in up right diagonal
    if up_right_diagonal_contains_a_player:
        up_right_diagonal_set = \
            {board_matrix[i][length-i-1] for i in range(0, length)}
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


def check_board_full_n_in_a_row(board_matrix):
    '''Check a nxn tictactoe board for n in a row

    -- board_matrix:  a nxn matrix representing a tic tac to board,  it
                     is assumed that 0 spaces are unocupied,  and numbered
                     spaces are occupied by a player represented by that number

    -- n_in_a_row: how many items in a row constitutes a win

    Returns: 0 if no three_in_a_row found,  otherwise the number of the player
             with the (first) three_in_a_row found'''
    num_sublists = len(board_matrix)
    for horizontal_row in board_matrix:
        num_items_in_sublists = len(horizontal_row)
        assert num_sublists == num_items_in_sublists, "matrix is not nxn"

    ret = Player.nobody.value
    if ret == Player.nobody.value:
        ret = check_board_horizontally_full(board_matrix)
    if ret == Player.nobody.value:
        ret = check_board_diagonally_full(board_matrix)
    if ret == Player.nobody.value:
        ret = check_board_vertically_full(board_matrix)
    return ret


def check_list_for_almost_n_in_a_row(values_sequence, n_in_a_row):
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


def get_part_of_board(board_matrix, starting_i, starting_j, delta_i, delta_j,
                      max_length):
    '''given a board_matrix, a position on that board matrix, a
    direction/velocity to travel from that position, and a number of values to
    try for: make a list of up to that size, by moving in that direction over
    the board, recording found values

    -- board_matrix: an nxn matrix carrying the current board state
    -- starting_i: starting row position on the board
    -- starting_j: starting column position on the board
    -- delta_i: rate and direction that we move over rows in the board
    -- delta_j: rate and direction that we move over columns in the board
    -- max_length: max length of the list that we make'''

    new_list = []
    # get parameters needed to move over matrix and record values
    possible_i_movement = abs((max_length-1) * delta_i)
    possible_j_movement = abs((max_length-1) * delta_j)
    i_max = min(len(board_matrix) - 1, starting_i + possible_i_movement)
    j_max = min(len(board_matrix) - 1, starting_j + possible_j_movement)
    i_min = max(0, starting_i - possible_i_movement)
    j_min = max(0, starting_j - possible_j_movement)

    # move over the matrix, recording the values found
    i = starting_i
    j = starting_j
    while i_min <= i <= i_max and j_min <= j <= j_max:
        new_list.append(board_matrix[i][j])
        i += delta_i
        j += delta_j
    return new_list


def note_potential_n_in_a_row(n_in_a_row_position_matrix, player, i, j):
    '''Call this function if a potential n_in_a_row is found (n-1 squares lined
    up horizontally, vertically, or diagonally, with the final square empty).
    It notes the location of the n_in_a_row, and the player who can
    make an n_in_a_row there in a provided n_in_a_row_position_matrix. If
    another n_in_a_row has been found already in the same position, this
    function will update the state of n_in_a_row_position_matrix to record that
    both players can make an n_in_a_row by playing there

    -- n_in_a_row_position_matrix: a board_matrix sized matrix used for noting
       where n_in_a_row's could potentially be produced next turn, and who they
       could be produced by

    -- player: the player who can potentially create an n_in_a_row
    -- i: row at which n_in_a_row could be produced
    -- j: column at which n_in_a_row could be produced'''

    assert player == Player(player).value,\
        "Unrecognized player given to n_in_a_row_position_matrix"
    assert player != Player.nobody.value, \
        "Noting that nobody is making a potential n_in_a_row is useless"

    current = n_in_a_row_position_matrix[i][j]
    currently_nobody_wins_at_this_position = (current == Player.nobody.value)
    currently_player1_wins_at_this_position = (current == Player.player1.value)
    currently_player2_wins_at_this_position = (current == Player.player2.value)
    a_new_player_wins_at_this_position = (current != player)

    if currently_nobody_wins_at_this_position:
        n_in_a_row_position_matrix[i][j] = player
    elif (currently_player1_wins_at_this_position or
            currently_player2_wins_at_this_position):
        if a_new_player_wins_at_this_position:
            n_in_a_row_position_matrix[i][j] = Player.both.value
    return


def check_diagonals_partially(board_matrix, n_in_a_row_position_matrix,
                              n_in_a_row):
    '''for an nxn matrix, look through the diagonal positions for almost
    n_in_a_row's (n spaces lined up, where n-1 of them have been played on by
    the same player, and the last one is empty. In other words, a situation
    where a player could potentially win on their next turn). Then note these
    positions, and the potentally winnning player, down on the
    given n_in_a_row_position_matrix.

    -- board_matrix: an nxn matrix (list of lists)
    -- n_in_a_row_position_matrix: another nxn matrix, used for recording the
       locations of any potential n_in_a_row's.
    -- n_in_a_row: What length constitutes an n_in_a_row

    Returns: reference to the n_in_a_row_position_matrix provided'''

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
    # for a board size of lxl (with l representing length), there's (l*2)-1
    # diagonals we can think of the first 3 (l) diagonals as starting at
    # locations a[0][?]
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
    #
    # The final thing to note is that we only look at chunks of the diagonal
    # that are at most n_in_a_row sized. Bigger chunks are broken up into
    # n_in_a_row sized chunks
    #
    # Ex. For n_in_a_row = 2 on a 4x4 board. We'd break up down right diagonal
    # as follows (into lists represented as a, b, and c):
    #
    #    0  1  2  3 (j)
    #  0 a |  |  |
    #    --+--+--+--
    #  1   |ab|  |
    #    --+--+--+--
    #  2   |  |bc|
    #    --+--+--+--
    #  3   |  |  |c
    # (i)

    length = len(board_matrix)
    num_diagonals_per_direction = (length*2)-1  # our (l*2)-1 diagonals

    # look at down right diagonals
    for n in range(num_diagonals_per_direction):
        # first ceiling(half) diagonals start at a[?][0]
        # second floor(half) diagonals start at a[0][?]
        i = max(n-length+1, 0)
        j = max(length-n-1, 0)
        delta_i = 1
        delta_j = 1
        while i + n_in_a_row - 1 < length and j + n_in_a_row - 1 < length:
            board_part = get_part_of_board(board_matrix, i, j,
                                           delta_i, delta_j, n_in_a_row)
            player, offset = check_list_for_almost_n_in_a_row(board_part,
                                                              n_in_a_row)
            if player is not None:
                offset_i = i + (offset * delta_i)
                offset_j = j + (offset * delta_j)
                note_potential_n_in_a_row(n_in_a_row_position_matrix, player,
                                          offset_i, offset_j)
            i += delta_i
            j += delta_j

    # look at up right diagonals
    for n in range(num_diagonals_per_direction):
        # first ceiling(half) diagonals start at a[?][length-1]
        # second floor(half) diagonals start at a[0][?]
        i = max(length-n-1, 0)
        j = min(length-1, num_diagonals_per_direction-n-1)
        delta_i = 1
        delta_j = -1
        while i < length and j >= 0:
            board_part = get_part_of_board(board_matrix, i, j,
                                           delta_i, delta_j, n_in_a_row)
            player, offset = check_list_for_almost_n_in_a_row(board_part,
                                                              n_in_a_row)
            if player is not None:
                offset_i = i + (offset * delta_i)
                offset_j = j + (offset * delta_j)
                note_potential_n_in_a_row(n_in_a_row_position_matrix, player,
                                          offset_i, offset_j)
            i += delta_i
            j += delta_j

    return n_in_a_row_position_matrix


def count_value(board_matrix, value):
    '''Counts number of zeros in an nxn matrix

    -- board_matrix: an nxn matrix
    -- value: value to count'''
    value_count = 0
    for row in board_matrix:
        for item in row:
            value_count += (item == value)
    return value_count


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


def copy_list_of_lists(board_matrix):
    '''Given a list of lists (a board_matrix), produce a copy of all items within
    that list and return the copy. Useful for avoiding python pass-by-reference
    issues

    -- board_matrix: an nxn matrix holding the current state of play'''
    new_board_matrix = []
    for row in board_matrix:
        new_row = list(row)
        new_board_matrix.append(new_row)
    return new_board_matrix


def gen_play_permutations(board_matrix, players_turn):
    '''Gens each possible move left in the board for a given player

    -- board_matrix: an nxn matrix holding the current state of play
    -- players_turn: indicates which players turn it is to play'''
    for i, row in enumerate(board_matrix):
        for j, square in enumerate(row):
            if square == Player.nobody.value:
                new_board_matrix = copy_list_of_lists(board_matrix)
                new_board_matrix[i][j] = players_turn
                yield new_board_matrix
    raise StopIteration


class Node:
    '''A node in our list-tree. The node stores information on what its parent
    is, what its children are, whether it's a winner, and how many winning
    children it has (0 initially, since it starts with no children)'''
    def __init__(self, parent, board_matrix, computer_value=1):
        '''initialize a node in the list tree

        -- parent: parent node, if any
        -- board_matrix: a nxn 2d list with the tic-tac-toe state for this node
        -- computer_value: the value that represents the computer on
        board_matrix, defaults to 1'''
        self.child_computer_wins = 0
        self.child_human_wins = 0
        self.winner = check_board_full_n_in_a_row(board_matrix)
        self.parent = parent

        self.children = []
        self.board_matrix = board_matrix

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def has_child(self, board_matrix):
        for child in self.children:
            if child.board_matrix == board_matrix:
                return child
        return None


def add_node_to_tree(board_matrix, parent_node):
    '''Adds a node to the current tree. If the parent_node is not there, adds a
    parent node. Otherwise adds the node as a child of the parent node

    -- board_matrix: the nxn board state for the node to be added
    -- parent_node: the nodes parent, if any'''
    if parent_node is None:
        parent_node = Node(None, board_matrix)
        new_child = parent_node
    else:
        child_node = Node(parent_node, board_matrix)
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

    # build and add children
    for board_variation in gen_play_permutations(parent_node.board_matrix,
                                                 player_turn):
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


def build_new_board_matrix(dimensions):
    '''Builds a board_matrix (list of lists of ints) of dimensions nxn,
    initialize to all 0's

    -- dimensions: the size of n for our nxn board_matrix'''
    sub_list = []
    board_matrix = []
    for i in range(dimensions):
        sub_list.append(0)
    for j in range(dimensions):
        board_matrix.append(sub_list)
    return board_matrix


def build_decision_tree(computer_goes_first=True, board_dimensions=3,
                        max_depth=None):
    '''Builds a decision tree for a board of given dimensions
    up to a maximum depth, or until all possibilities are exhausted

    -- board_dimensions: how big a board to calculate for, base is 3, the
    generic tic tac toe size

    -- depth: How deep a decision tree to build. Pass None for a full
    tree.

    Returns: root node of tree'''
    board_matrix = build_new_board_matrix(board_dimensions)

    if computer_goes_first:
        computer_player = Player.player1.value
    else:
        computer_player = Player.player2.value

    root = Node(None, board_matrix, computer_player)
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
    #           .format(child.board_matrix, child.child_computer_wins,
    #                   child.child_human_wins))
    # print_tree_structure(root)
