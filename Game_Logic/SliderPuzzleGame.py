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
    def __init__(self, size):
        self.parent = None
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]

    def initialize_board(self, board):
        self.board = [[board[i][j] for j in range(self.size)] for i in range(self.size)]

    def is_over(self):
        board = [[1 + j + self.size * i for j in range(self.size)] for i in range(self.size)]
        board[self.size - 1][self.size - 1] = 0
        return self.board == board

    def index_of_empty_cell(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return i, j
        raise Exception("There was no Empty Cell")

    def can_move(self, x, y):
        x1, y1 = self.index_of_empty_cell()
        if x == x1 and y == y1:
            return False
        if distance_between_2_points(x, y, x1, y1) != 1:
            return False
        return self.size > x >= 0 and self.size > y >= 0

    def move(self, x, y):
        if not self.can_move(x, y):
            return False
        x1, y1 = self.index_of_empty_cell()
        (self.board[x][y], self.board[x1][y1]) = (self.board[x1][y1], self.board[x][y])
        return True

    def get_indexes_of_all_possible_moves(self):
        return [[x, y] for x in range(self.size) for y in range(self.size) if self.can_move(x, y)]

    def get_all_possible_states(self):
        result = []
        for x, y in self.get_indexes_of_all_possible_moves():
            new_state = SliderPuzzleGame(self.size)
            new_state.initialize_board(self.board)
            new_state.move(x, y)
            result.append(new_state)
        return result

    def generate_random_board(self):
        board = [[1 + j + self.size * i for j in range(self.size)] for i in range(self.size)]
        board[self.size - 1][self.size - 1] = 0
        board = public_shuffle_2d_list(board)
        while self.is_solvable(board) is False:
            board = public_shuffle_2d_list(board)
        return board

    def count_inversions(self, arr):
        counter = 0
        for i in range(self.size * self.size):
            for j in range(i + 1, self.size * self.size):
                if 0 < arr[i] and 0 < arr[j] < arr[i]:
                    counter += 1
        return counter

    def is_solvable(self, board):
        result = list_2d_to_1d(board)
        inversion_counter = self.count_inversions(result)
        return inversion_counter % 2 == 0

    def __str__(self):
        result = ""
        for ca in list_2d_to_1d(self.board):
            result += str(ca)
        return result

    def print_board(self):
        for row in self.board:
            print(" ".join(str(num).ljust(self.size) for num in row))



