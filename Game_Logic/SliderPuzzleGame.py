from Game_Logic.HelperFunctions import *


def misplaced_tiles(another):
    total_of_misplaced_tiles = 0
    for i in range(another.size):
        for j in range(another.size):
            value = 9 if another.board[i][j] == 0 else another.board[i][j]
            total_of_misplaced_tiles += 0 if value == (1 + j + another.size * i) else 1

    return total_of_misplaced_tiles


def manhattan_distance(another):
    total = 0
    for i in range(another.size):
        for j in range(another.size):
            value = another.board[i][j]
            if value != 0:
                x, y = coordinates_1d_to_2d(value, another.size)
                total += abs(i - x) + abs(j - y)
            else:
                total += abs(i - 2) + abs(j - 2)

    return total


class SliderPuzzleGame:
    # This function initialize the game.
    def __init__(self, size):
        self.parent = None
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.goal_board = [[1 + j + size * i for j in range(size)] for i in range(size)]
        self.goal_board[size - 1][size - 1] = 0

    # This function initialize the board
    def initialize_board(self, board):
        self.board = [[board[i][j] for j in range(self.size)] for i in range(self.size)]

    # This function initialize the goal board
    def initialize_goal_board(self, board):
        self.goal_board = [[board[i][j] for j in range(self.size)] for i in range(self.size)]

    # This function determines if we reached the goal state
    def is_over(self):
        return self.board == self.goal_board

    # This function return the (x, y) of the empty cell
    def index_of_empty_cell(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return i, j
        raise Exception("There was no Empty Cell")

    # This function determines if the giving move is valid
    def can_move(self, x, y):
        x1, y1 = self.index_of_empty_cell()
        if x == x1 and y == y1:
            return False
        if distance_between_2_points(x, y, x1, y1) != 1:
            return False
        return self.size > x >= 0 and self.size > y >= 0

    # This function moves the giving cell
    def move(self, x, y):
        if not self.can_move(x, y):
            return False
        x1, y1 = self.index_of_empty_cell()
        (self.board[x][y], self.board[x1][y1]) = (self.board[x1][y1], self.board[x][y])
        return True

    # This function returns the indexes of all possible moves
    def get_indexes_of_all_possible_moves(self):
        xs = [0, -1, 0, 1]
        ys = [-1, 0, 1, 0]
        possible_moves = []
        (x, y) = self.index_of_empty_cell()
        for i in range(4):
            if self.can_move(xs[i] + x, ys[i] + y):
                possible_moves.append([xs[i] + x, ys[i] + y])
        return possible_moves

    # This function returns all possible states of the game
    def get_all_possible_states(self):
        result = []
        for x, y in self.get_indexes_of_all_possible_moves():
            new_state = SliderPuzzleGame(self.size)
            new_state.initialize_board(self.board)
            new_state.move(x, y)
            result.append(new_state)
        return result

    # This function generate a solvable random board
    def generate_random_board(self):
        board = [[1 + j + self.size * i for j in range(self.size)] for i in range(self.size)]
        board[self.size - 1][self.size - 1] = 0
        board = public_shuffle_2d_list(board)
        while self.is_solvable(board) is False:
            board = public_shuffle_2d_list(board)
        return board

    # This function determines if the giving board is solvable
    def is_solvable(self, board):
        def count_inversions(arr):
            counter = 0
            for i in range(self.size * self.size):
                for j in range(i + 1, self.size * self.size):
                    if 0 < arr[i] and 0 < arr[j] < arr[i]:
                        counter += 1
            return counter

        result = list_2d_to_1d(board)
        inversion_counter = count_inversions(result)
        if self.size % 2 == 0:
            (x, y) = self.index_of_empty_cell()
            return (inversion_counter + x) % 2 != 0
        else:
            return inversion_counter % 2 == 0

    # This function returns the board as a string like this "123456780"
    def __str__(self):
        result = ""
        for ca in list_2d_to_1d(self.board):
            result += str(ca)
        return result

    # This function prints the board
    def print_board(self):
        for row in self.board:
            print(" ".join(str(num).ljust(self.size) for num in row))

    # This function prints the goal_board
    def print_goal_board(self):
        for row in self.goal_board:
            print(" ".join(str(num).ljust(self.size) for num in row))
