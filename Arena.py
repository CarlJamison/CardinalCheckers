from Checkers import *
import AverageAI
import RandomAI
import MinMaxAI
import AlphaBetaAI

def profile_helper():
    boardString = "2 0-0-0-0- 0-0-0-0- 0-0-0-0- 1-1-1-1- 1-1-1-1- 2-2-2-2- 2-2-2-2- 2-2-2-2-"
    board = CheckerBoard(boardString)
    MinMaxAI.GetMove(board)

def single_move():
    boardString = "0 1-0-1-1- 0-1-1-0- 2-1-0-1- 1-0-1-1- 1-1-1-2- 2-1-1-1- 1-1-1-1- 2-2-2-2-"
    board = CheckerBoard(boardString)
    print(board.toString())
    AlphaBetaAI.GetMove(board)
    print(board.toString())

def AIProfiler():
    import profile
    profile.run('profile_helper()')

def main():
    #boardString = "2 0-0-1-0- 0-1-0-0- 1-1-1-0- 1-2-1-1- 1-1-1-1- 1-2-1-2- 1-1-1-2- 1-1-0C2-"
    boardString = "2 0-0-0-0- 0-0-0-0- 0-0-0-0- 1-1-1-1- 1-1-1-1- 2-2-2-2- 2-2-2-2- 2-2-2-2-"
    board = CheckerBoard(boardString)

    while not board.gameOver:
        print(board.toString())
        if board.player == -1:
            move = MinMaxAI.GetMove(board)
        else:
            move = AlphaBetaAI.GetMove(board)

        board.makeMove(move)

    print(board.toString())

main()

    


