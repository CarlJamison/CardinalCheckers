class Move:
    def __init__(self, startX, startY, endX, endY):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY 

class CheckerBoard:
    
    def __init__(self, boardString):
        self.move = 0

        self._isJumpPossible = False
        self.jpCheck = -1

        self.jumped = False
        self.iJump = 0
        self.jJump = 0
        self.board = [[0]*8 for i in range(8)]
        self.crowned = [[0]*8 for i in range(8)]
        self.player = int(boardString[0: 1]) - 1
        self.gameOver = False
        coord = 2
        for i in range(8):
            for j in range(8):
                if (i % 2 == j % 2):
                    self.board[i][j] = int(boardString[coord: coord + 1]) - 1
                    coord+=1
                    self.crowned[i][j] = boardString[coord: coord + 1] == "C"
                    coord+=1
            coord+=1

    def checkDirection(self, iO, jO, i, j):
        if (self.board[i][j] == self.player and (self.crowned[i][j] or iO == -self.player)):
            return (i + (2 * iO) < 8 and i + (2 * iO) >= 0 and j + (2 * jO) < 8 and j + (2 * jO) >= 0
					and self.board[i + (2 * iO)][j + (2 * jO)] == 0 and self.board[i + iO][j + jO] == -self.player)
        return False

    def checkMoveDirection(self, iO, jO, i, j):
        if (self.board[i][j] == self.player and (self.crowned[i][j] or iO == -self.player)):
            return (i + iO < 8 and i + iO >= 0 and j + jO < 8 and j + jO >= 0 and self.board[i + iO][j + jO] == 0)
        return False

    def checkDirectionList(self, iO, jO, i, j, list):
        if(self.checkDirection(iO, jO, i, j)):
            list.append(Move(i, j, i + (2 * iO), j + (2 * jO)))

    def checkMoveDirectionList(self, iO, jO, i, j, list):
        if(self.checkMoveDirection(iO, jO, i, j)):
            list.append(Move(i, j, i + iO, j + jO))

    def getMoveList(self):
        list = []

        jump = self.isJumpPossible()
        for i in range(8):
            for j in range(8):
                self.checkDirectionList(1, 1, i, j, list)
                self.checkDirectionList(1, -1, i, j, list)
                self.checkDirectionList(-1, 1, i, j, list)
                self.checkDirectionList(-1, -1, i, j, list)
                
                if (not jump):
                    self.checkMoveDirectionList(1, 1, i, j, list)
                    self.checkMoveDirectionList(1, -1, i, j, list)
                    self.checkMoveDirectionList(-1, 1, i, j, list)
                    self.checkMoveDirectionList(-1, -1, i, j, list)
                    
        return list

    def checkWin(self):
        player1 = False
        player2 = False
        for i in range(8):
            for j in range(8):
                if (self.board[i][j] == -1):
                    player1 = True
                elif (self.board[i][j] == 1):
                    player2 = True
                    
        self.gameOver = not player1 or not player2
        return self.gameOver

    def isJumpPossible(self):
        if self.move == self.jpCheck:
            return self._isJumpPossible

        if self.jumped:
            retVal = self.checkDirection(1, 1, self.iJump, self.jJump) or self.checkDirection(1, -1, self.iJump, self.jJump) or self.checkDirection(-1, 1, self.iJump, self.jJump) or self.checkDirection(-1, -1, self.iJump, self.jJump)
            self._isJumpPossible = retVal
            self.jpCheck = self.move
            return retVal
        
        for i in range(8):
            for j in range(8):
                if (self.checkDirection(1, 1, i, j) or self.checkDirection(1, -1, i, j) or self.checkDirection(-1, 1, i, j)
						or self.checkDirection(-1, -1, i, j)):
                    self._isJumpPossible = True
                    self.jpCheck = self.move
                    return True

        self._isJumpPossible = False
        self.jpCheck = self.move
        return False

    def isMovePossible(self):
        if (self.isJumpPossible()):
            return True
        
        for i in range(8):
            for j in range(8):
                if (self.checkMoveDirection(1, 1, i, j) or self.checkMoveDirection(1, -1, i, j) or self.checkMoveDirection(-1, 1, i, j)
						or self.checkMoveDirection(-1, -1, i, j)):
                    return True
        
        return False

    def makeMove(self,move):
        startX = move.startX
        startY = move.startY
        endX = move.endX
        endY = move.endY

        #Check bounds
        if (self.board[startX][startY] == self.player and self.board[endX][endY] == 0):
            valid = False

			#Check if a jump
            if (abs(startX - endX) == 2 and abs(startY - endY) == 2):
                if (self.board[int((startX + endX) / 2)][int((startY + endY) / 2)] == -self.player):
                    if (self.crowned[startX][startY] or (startX - endX) == self.player * 2):
                        self.board[int((startX + endX) / 2)][int((startY + endY) / 2)] = 0
                        self.crowned[int((startX + endX) / 2)][int((startY + endY) / 2)] = False
                        self.jumped = True
                        self.iJump = endX
                        self.jJump = endY
                        valid = True
            elif (abs(startX - endX) == 1 and abs(startY - endY) == 1):

                # Check that it's not a backwards move
                if (self.crowned[startX][startY] or (startX - endX) == self.player):
                    # Check if jump is possible
                    if (not self.isJumpPossible()):
                        valid = True

            if (valid):
                self.board[startX][startY] = 0
                self.board[endX][endY] = self.player
                self.move += 1
                self.crowned[endX][endY] = self.crowned[startX][startY]
                self.crowned[startX][startY] = False

                if ((endX == 8 - 1 and self.player == -1) or (endX == 0 and self.player == 1)):
                    self.crowned[endX][endY] = True

                if (not self.checkWin() and not (self.jumped and self.isJumpPossible())):
                    self.player = -self.player
                    self.jumped = False

                    if (not self.isMovePossible()):
                        self.player = -self.player
                        if(not self.isMovePossible()):
                            self.gameOver = True
            else:
                print("Move failed")

    def toString(self):
        returnString = str(self.player + 1)
        
        for i in range(8):
            returnString += "\n"
            for j in range(8):
                val = self.board[i][j]
                returnString += "O" if val == -1 else " " if val == 0 else "X" 
                if (self.crowned[i][j]):
                    returnString += "C"
                else:
                    returnString += "-"
        
        return returnString