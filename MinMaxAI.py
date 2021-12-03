import copy
import pickle
from Checkers import *
NUMBER_OF_ROUNDS = 5

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

    if board.gameOver: runningScore += 1000 if(board.player == player) else -1000
    if board.isJumpPossible(): runningScore += 10 if(board.player == player) else -10

    return runningScore

def getScoreRec(board: CheckerBoard, player, remainingRounds):
    if board.gameOver or remainingRounds == 0:
        return getNaiveScore(board, player)

    score = 0
    moveList = board.getMoveList()
    first = True
    if(board.player == player):
        for move in moveList:
            clone = pickle.loads(pickle.dumps(board))
            clone.makeMove(move)
            localScore = getScoreRec(clone, player, remainingRounds - 1)
            if localScore > 1000: return localScore
            if localScore > score or first: 
                score = localScore
                first = False
        return score
    else:
        for move in moveList:
            clone = pickle.loads(pickle.dumps(board))
            clone.makeMove(move)
            localScore = getScoreRec(clone, player, remainingRounds - 1)
            if localScore < score or first: 
                score = localScore
                first = False
        return score

def getScore(board, player):
    return getScoreRec(board, player, NUMBER_OF_ROUNDS)

def GetMove(board: CheckerBoard):
    moveList = board.getMoveList()
    
    if len(moveList) == 1: return moveList[0]

    highScore = 0
    highMove = 0
    for move in moveList[0:]:
        clone = pickle.loads(pickle.dumps(board))
        clone.makeMove(move)
        score = getScore(clone, board.player)

        print(str(move.startX) + ":" + str(move.startY) + " -> " + str(move.endX) + ":" + str(move.endY) + " Score: " + str(score))

        if(score > highScore or highMove == 0):
            highScore = score
            highMove = move
            
    print("\nMove chosen: " + str(highMove.startX) + ":" + str(highMove.startY) + " -> " + str(highMove.endX) + ":" + str(highMove.endY) + " Score: " + str(highScore))

    return highMove










