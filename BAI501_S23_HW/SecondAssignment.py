import Game_Logic.SliderPuzzleGame as Game
import Algorithms.AStar as AStar


def print_goal_state():
    print("Goal State: ")
    goal = Game.SliderPuzzleGame(3)
    goal.initialize_board([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    goal.print_board()
    print("\n")


initial = Game.SliderPuzzleGame(3)
board = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
initial.initialize_board(initial.generate_random_board())
print("Initial State: ")
initial.print_board()
print("\n\nMoves to solve:\n")
initial.print_board()
path, discovered, visited = AStar.find_path(initial, Game.manhattan_distance)
for counter in range(len(path)):
    print("\n\nMove: ", counter + 1, "\n")
    if len(path) - 1 != counter:
        path[counter].print_board()

print_goal_state()
