import math
import pickle
from Checkers import *
NUMBER_OF_ROUNDS = 7

def getNaiveScore(board: CheckerBoard, player):

    if board.gameOver: 
        if(board.player == player):
            return 1000
        else:
            return -1000
            
    runningScore = 0

    for i in range(8):
        for j in range(8):
            if (board.board[i][j] == player):
                runningScore += 7
                if board.crowned[i][j]: runningScore += 3

            elif (board.board[i][j] != 0):
                runningScore -= 7
                if board.crowned[i][j]: runningScore -= 3
    
    if board.isJumpPossible(): runningScore += 10 if(board.player == player) else -10

    return runningScore

def getScoreRec(board: CheckerBoard, player, remainingRounds, ALPHA, BETA):
    if board.gameOver or remainingRounds == 0:
        return getNaiveScore(board, player)

    moveList = board.getMoveList()
    if(board.player == player):
        score = -math.inf
        for move in moveList:
            clone = pickle.loads(pickle.dumps(board))
            clone.makeMove(move)
            score = max(getScoreRec(clone, player, remainingRounds - 1, ALPHA, BETA), score)
            if score >= BETA: return score
            ALPHA = max(ALPHA, score)
            if score == 1000: return score
        return score
    else:
        score = math.inf
        for move in moveList:
            clone = pickle.loads(pickle.dumps(board))
            clone.makeMove(move)
            score = min(getScoreRec(clone, player, remainingRounds - 1, ALPHA, BETA), score)
            if(score <= ALPHA): return score
            BETA = min(BETA, score)
            if score == -1000: return score
        return score

def getScore(board, player, ALPHA, BETA):
    return getScoreRec(board, player, NUMBER_OF_ROUNDS, ALPHA, BETA)

def GetMove(board: CheckerBoard):
    ALPHA = -math.inf
    BETA = math.inf
    moveList = board.getMoveList()
    
    if len(moveList) == 1: return moveList[0]

    highScore = -math.inf
    highMove = 0
    for move in moveList[0:]:
        clone = pickle.loads(pickle.dumps(board))
        clone.makeMove(move)
        score = getScore(clone, board.player, ALPHA, BETA)
        ALPHA = max(ALPHA, score)
        print(str(move.startX) + ":" + str(move.startY) + " -> " + str(move.endX) + ":" + str(move.endY) + " Score: " + str(score))

        if(score > highScore):
            highScore = score
            highMove = move
            
    print("\nMove chosen: " + str(highMove.startX) + ":" + str(highMove.startY) + " -> " + str(highMove.endX) + ":" + str(highMove.endY) + " Score: " + str(highScore))

    return highMove










