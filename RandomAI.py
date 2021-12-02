import random
from Checkers import *

def GetMove(board: CheckerBoard):
    moveList = board.getMoveList()
    move = random.choice(moveList)      
    #print("\nMove chosen: " + str(move.startX) + ":" + str(move.startY) + " -> " + str(move.endX) + ":" + str(move.endY))
    return move










