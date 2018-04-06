import copy

class GameOfLife(object):
    def __init__(self, height, width, board=None):
        self.height = height
        self.width  = width
        if(board):
            assert(len(board) == self.height)
            assert(len(board[0]) == self.width)
            self.board = board
        else:
            self.board = []
            for i in range(self.height):
                row = [False] * self.width
                self.board.append(row)

    def onBoard(self, row, col):
        if(0 <= row and row < len(self.board)):
            if(0 <= col and col < len(self.board[row])):
                return True
        return False

    @staticmethod
    def neighbors(board, row, col):
        height = len(board)
        width = len(board[0])
        self = GameOfLife(height, width, board)

        if(self.onBoard(row,col)):
            count = 0

            nrow = row-1
            ncol = col-1
            if(self.onBoard(nrow,ncol)):
                if(self.board[nrow][ncol]): count += 1

            nrow = row-1
            ncol = col
            if(self.onBoard(nrow,ncol)):
                if(self.board[nrow][ncol]): count += 1

            nrow = row-1
            ncol = col+1
            if(self.onBoard(nrow,ncol)):
                if(self.board[nrow][ncol]): count += 1

            nrow = row
            ncol = col-1
            if(self.onBoard(nrow,ncol)):
                if(self.board[nrow][ncol]): count += 1


            nrow = row
            ncol = col+1
            if(self.onBoard(nrow,ncol)):
                if(self.board[nrow][ncol]): count += 1

            nrow = row+1
            ncol = col-1
            if(self.onBoard(nrow,ncol)):
                if(self.board[nrow][ncol]): count += 1

            nrow = row+1
            ncol = col
            if(self.onBoard(nrow,ncol)):
                if(self.board[nrow][ncol]): count += 1

            nrow = row+1
            ncol = col+1
            if(self.onBoard(nrow,ncol)):
                if(self.board[nrow][ncol]): count += 1

            return count

    def stepBoard(self):
        refBoard = copy.deepcopy(self.board)
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if(refBoard[row][col]):
                    nCount = GameOfLife.neighbors(refBoard, row, col)
                    if(nCount < 2):
                        self.board[row][col] = False
                    elif(nCount > 3):
                        self.board[row][col] = False
                    else:
                        self.board[row][col] = True
                else:
                    if(GameOfLife.neighbors(refBoard, row, col) == 3):
                        self.board[row][col] = True
                    else:
                        self.board[row][col] = False

    def setCell(self, row, col, alive):
        if(self.onBoard(row, col)):
            self.board[row][col] = alive


    def boardString(self):
        rowStrings = []
        for row in self.board:
            rowStr = ""
            for col in row:
                if(col): rowStr += "M"
                else:    rowStr += "."
            rowStrings.append(rowStr)
        return "\n".join(rowStrings)

def stepPrint(x):
    print(x.boardString())
    x.stepBoard()

def listenLoop(x):
    while True:
        print(x.boardString())
        x.stepBoard()
        input()


a = [[False, True,  False, False, False],
     [False, True,  False, True,  False],
     [False, False, False, False, False],
     [False, True,  False, True,  True],
     [False, False, False, False, False]]

b = GameOfLife(5,5, a)


glider = GameOfLife(40, 100)
glider.setCell(0,1,True)
glider.setCell(1,2,True)
glider.setCell(2,0,True)
glider.setCell(2,1,True)
glider.setCell(2,2,True)

r = GameOfLife(40, 100)
r.setCell(20, 50,True)
r.setCell(19, 50,True)
r.setCell(21, 50,True)
r.setCell(19, 51,True)
r.setCell(20, 49,True)

horizontal = GameOfLife(40, 100)
for i in range(8): horizontal.setCell(20, 4+i, True)
for i in range(5): horizontal.setCell(20, 13+i, True)
for i in range(3): horizontal.setCell(20, 21+i, True)
for i in range(6): horizontal.setCell(20, 30+i, True)
for i in range(5): horizontal.setCell(20, 37+i, True)










