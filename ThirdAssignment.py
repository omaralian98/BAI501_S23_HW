import Game_Logic.SliderPuzzleGame as Game
import Algorithms.AStar as AStar
import EBFCalculator.EBF as EBF


print("\td\t\t EBF Misplaced Tiles\t\tEBF Manhattan Distance")
initial = Game.SliderPuzzleGame(3)
for i in range(1, 101):
    initial.initialize_board(initial.generate_random_board())
    path, discovered, visited = AStar.find_path(initial, Game.misplaced_tiles)
    path1, discovered1, visited1 = AStar.find_path(initial, Game.manhattan_distance)
    print(format(i, '<3') + '-\t' + str(len(path)) + ' \t\t\t' + format(EBF.get(len(path), discovered), '.4f') +
          '\t\t\t\t' + format(EBF.get(len(path1), discovered1), '.4f'))
