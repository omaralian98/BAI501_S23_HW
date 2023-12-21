import Game_Logic.SliderPuzzleGame as Game
import Algorithms.AStar_Search as AStar
import time


def print_goal_state():
    print("Goal State: ")
    goal = Game.SliderPuzzleGame(3)
    goal.print_goal_board()
    print("\n")


initial = Game.SliderPuzzleGame(3)
board = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
initial.initialize_board(board)
print("Initial State: ")
initial.print_board()
print("\n")
print_goal_state()
start_time = time.time()
path, discovered, visited = AStar.find_path(initial, Game.misplaced_tiles)
mistime = (time.time() - start_time)
start_time1 = time.time()
path1, discovered1, visited1 = AStar.find_path(initial, Game.manhattan_distance)
mantime = (time.time() - start_time1)
print("Took: %s s to find" % format(mistime, '.3f'))
print("Moves to solve using misplaced tiles heuristic: ", len(path))
print("Expanded nodes to solve using misplaced tiles heuristic: ", visited)
print("Took: %s s to find" % format(mantime, '.3f'))
print("Moves to solve using manhattan distance heuristic: ", len(path1))
print("Expanded nodes to solve using manhattan distance heuristic: ", visited1)
