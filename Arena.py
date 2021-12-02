from Checkers import *
import AverageAI
import RandomAI

#boardString = "2 0-0-1-0- 0-1-0-0- 1-1-1-0- 1-2-1-1- 1-1-1-1- 1-2-1-2- 1-1-1-2- 1-1-0C2-"
boardString = "2 0-0-0-0- 0-0-0-0- 0-0-0-0- 1-1-1-1- 1-1-1-1- 2-2-2-2- 2-2-2-2- 2-2-2-2-"
board = CheckerBoard(boardString)

while not board.gameOver:
    print(board.toString())
    if board.player == -1:
        move = AverageAI.GetMove(board)
    else:
        move = RandomAI.GetMove(board)

    board.makeMove(move)

print(board.toString())

    


