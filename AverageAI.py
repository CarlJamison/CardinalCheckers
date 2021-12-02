import copy
from Checkers import *
NUMBER_OF_ROUNDS = 4

def getNaiveScore(board: CheckerBoard, player):
    runningScore = 0

    for i in range(8):
        for j in range(8):
            if (board.board[i][j] == player):
                runningScore += 7
                if board.crowned[i][j]: runningScore += 3

            elif (board.board[i][j] != 0):
                runningScore -= 7
                if board.crowned[i][j]: runningScore -= 3

    if board.gameOver: runningScore += 100 if(board.player == player) else -100
    if board.isJumpPossible(): runningScore += 10 if(board.player == player) else -10

    return runningScore

def getScoreRec(board: CheckerBoard, player, remainingRounds):
    if board.gameOver or remainingRounds == 0:
        return getNaiveScore(board, player)

    totalScore = 0
    moveList = board.getMoveList()
    for move in moveList:
        clone = copy.deepcopy(board)
        clone.makeMove(move)
        totalScore += getScoreRec(clone, board.player, remainingRounds - 1)

    return totalScore / len(moveList)

def getScore(board, player):
    return getScoreRec(board, player, NUMBER_OF_ROUNDS)

def GetMove(board: CheckerBoard):
    moveList = board.getMoveList()

    highScore = 0
    highMove = 0
    for move in moveList[0:]:
        clone = copy.deepcopy(board)
        clone.makeMove(move)
        score = getScore(clone, board.player)

        #print(str(move.startX) + ":" + str(move.startY) + " -> " + str(move.endX) + ":" + str(move.endY) + " Score: " + str(score))

        if(score > highScore or highMove == 0):
            highScore = score
            highMove = move
            
    #print("\nMove chosen: " + str(highMove.startX) + ":" + str(highMove.startY) + " -> " + str(highMove.endX) + ":" + str(highMove.endY) + " Score: " + str(highScore))

    return highMove










