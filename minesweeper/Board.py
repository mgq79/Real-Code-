import random

# Board
# 2d array of ints, -1 is bomb, 0 is empty, number is number of adjacent mines

class Board(object):

    def __init__(this, rows, cols):
        this.board = [0] * rows
        this.revealed = [False] * rows
        this.marked = [False] * rows
        for row in range(rows):
            this.board[row] = [0] * cols
            this.revealed[row] = [False] * cols
            this.marked[row] = [False] * cols

    @staticmethod
    def get(L, i, d):
        if(i < 0):
            return d
        elif(i >= len(L)):
            return d
        else:
            return L[i]

    @staticmethod
    def isMine(n):
        return n == -1


    def placeMines(this, n):
        rows = len(this.board)
        cols = len(this.board[0])
        while(n > 0):
            row = random.randrange(rows)
            col = random.randrange(cols)
            if(this.board[row][col] != -1):
                this.board[row][col] = -1
                n -= 1


    def placeNumbers(this):
        rows = len(this.board)
        cols = len(this.board[0])
        for row in range(rows):
            for col in range(cols):
                if(Board.isMine(this.board[row][col])):
                    continue
                else:
                    count = 0
                    for xOff in [-1, 0, 1]:
                        for yOff in [-1, 0, 1]:
                            t = Board.get(Board.get(this.board, row+yOff, []), col+xOff, 0)
                            if(Board.isMine(t)):
                                count += 1
                    this.board[row][col] = count

    def printBoard(this):
        for row in this.board:
            for col in row:
                print(str(col) + '\t', end='')
            print()

    def reveal(this, row, col):
        if(Board.get(Board.get(this.revealed, row, []), col, True)):
            return
        elif(Board.get(Board.get(this.marked, row, []), col, True)):
            return
        else:
            this.revealed[row][col] = True
            if(this.board[row][col] != 0):
                return
            else:
                for xOff in [-1, 0, 1]:
                    for yOff in [-1, 0, 1]:
                        this.reveal(row+yOff, col+xOff)

    def checkWin(this):
        for row in range(len(this.board)):
            for col in range(len(this.board[row])):
                if(this.marked[row][col] and not Board.isMine(this.board[row][col])):
                    return False
                if(not this.marked[row][col] and Board.isMine(this.board[row][col])):
                    return False
        return True


if(__name__ == "__main__"):
    print("Making Board...")
    b = Board(5, 5)
    b.printBoard()
    print()
    print("Placing 3 Mines...")
    b.placeMines(3)
    b.printBoard()
    print()
    print("Placing adjacency numbers...")
    b.placeNumbers()
    b.printBoard()
    print()
    print("Revealing 0, 0")
    for row in b.revealed:
        print(row)
    b.reveal(0, 0)
    print()
    for row in b.revealed:
        print(row)



