import BoardOCR
from Checkers import CheckerBoard
import MinMaxAI

boardString = BoardOCR.getBoardStringFromImage('straight.jpg')

board = CheckerBoard(boardString)

move = MinMaxAI.GetMove(board)

