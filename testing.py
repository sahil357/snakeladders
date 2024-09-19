from board import SnakesAndLadderBoard
from game import Game


board1 = SnakesAndLadderBoard()
board1.create_ladder(4, 20)
board1.create_ladder(23, 50)
board1.create_ladder(55, 90)

board1.create_snakes(20, 9)
board1.create_snakes(60, 8)
board1.create_snakes(38, 6)

game1 = Game(board1)
game1.add_player('sahil', 'ss')
game1.add_player('singla', 'sss')

game1.start_game()

print(board1)
print(game1)

#------------------
# Game:

