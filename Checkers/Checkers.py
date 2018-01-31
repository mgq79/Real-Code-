import copy

# Base Game Class
# Requirements:
#   moves:
#     returns a list of all valid moves given a board state
#   start:
#     starting board state (empty)
#   makeMove:
#     takes a move and a board and returns a new board with the given
#     move applied
#   estimate (this is the important one):
#     takes a board state and gives an estimated value for use with
#     the minimax and/or alphabeta approach to game logic
#
#   move encoding: -note Y and X are each in [0, 8)
#     +rYX = add red piece at board[Y][X]
#     +RYX = add red king
#     +bYX = add black piece
#     +BYX = add black king
#     -rYX= remove red piece
#     -bYX = remove black piece

class Game(object):
    #Python doesn't actually have interfaces afaik
    #TODO find out about abstract classes/interfaces in python


    @staticmethod
    def defaultEst(board):
        return 0

    # A board for Checkers is an 8x8 grid of squares
    # (Only half will be used because otherwise it's hard)
    # a square is either empty, red, black, redKing, or blackKing
    # We'll denote a non-playing square with "X"
    @staticmethod
    def getStart():
        start = [["black", "X", "black", "X", "black", "X", "black", "X"],
                 ["X", "black", "X", "black", "X", "black", "X", "black"],
                 ["black", "X", "black", "X", "black", "X", "black", "X"],
                 ["X", None, "X", None, "X", None, "X", None],
                 [None, "X", None, "X", None, "X", None, "X"],
                 ["X", "red", "X", "red", "X", "red", "X", "red"],
                 ["red", "X", "red", "X", "red", "X", "red", "X"],
                 ["X", "red", "X", "red", "X", "red", "X", "red"]]
        return start


    @staticmethod
    def otherPlayer(p):
        if(p == "red"):
            return "black"
        elif(p == "black"):
            return "red"

    @staticmethod
    def onBoard(row, col):
        return row >= 0 and row < 8 and col >= 0 and col < 8


    def __init__(self, est = None):
        if(est):
            self.est = est
        else:
            self.est = Game.defaultEst
        self.currPlayer = "black"
        self.board = Game.getStart()

    @staticmethod
    def redCapturesFromSquare(board, row, col):
        temp = copy.deepcopy(board)
        if(board[row][col] == "redKing"):
            Ys = [-2, 2]
            piece = "R"
        else:
            Ys = [-2] #Only up
            piece = "r"

        moves = []
        for dx in [-2, 2]:
            for dy in Ys:
                if(Game.onBoard(row+dy, col+dx) and board[row+dy][col+dx] == None):
                    if(row+dy == 0):
                        p = "R"
                    else:
                        p = piece
                    if(temp[row+(dy//2)][col+(dx//2)] and \
                       temp[row+(dy//2)][col+(dx//2)].startswith("black")):
                        minString = "-"+piece+str(row)+str(col)+",-b" \
                                   +str(row+(dy//2))+str(col+(dx//2)) \
                                   +",+"+p+str(row+dy)+str(col+dx)

                        if(row+dy == 0):
                            temp[row+dy][col+dx] = "redKing"
                        else:
                            temp[row+dy][col+dx] = temp[row][col]
                        temp[row][col] = None
                        temp[row+(dy//2)][col+(dx//2)] = None

                        moves.append(minString)
                        moreMoves = Game.redCapturesFromSquare(temp, row+dy, col+dx)
                        for m in moreMoves:
                            moves.append(minString + "," + m)
        return moves


    @staticmethod
    def redMovesFromSquare(board, row, col):

        if(board[row][col] == "redKing"):
            Ys = [-1, 1]
            piece = "R"
        else:
            Ys = [-1] #Only up
            piece = "r"

        moves = []
        for dx in [-1, 1]:
            for dy in Ys:
                if(Game.onBoard(row+dy, col+dx)):
                    if(row+dy == 0):
                        p = "R"
                    else:
                        p = piece
                    if(board[row+dy][col+dx] == None):
                        moves.append("-"+piece+str(row)+str(col)+",+" \
                                +p+str(row+dy)+str(col+dx))

        moves.extend(Game.redCapturesFromSquare(board, row, col))
        return moves


    @staticmethod
    def blackCapturesFromSquare(board, row, col):
        temp = copy.deepcopy(board)
        if(board[row][col] == "blackKing"):
            Ys = [-2, 2]
            piece = "B"
        else:
            Ys = [2] #Only down
            piece = "b"

        moves = []
        for dx in [-2, 2]:
            for dy in Ys:
                if(Game.onBoard(row+dy, col+dx) and board[row+dy][col+dx] == None):
                    if(row+dy == 0):
                        p = "B"
                    else:
                        p = piece
                    if(temp[row+(dy//2)][col+(dx//2)] and \
                       temp[row+(dy//2)][col+(dx//2)].startswith("red")):
                        minString = "-"+piece+str(row)+str(col)+",-r" \
                                   +str(row+(dy//2))+str(col+(dx//2)) \
                                   +",+"+p+str(row+dy)+str(col+dx)

                        if(row+dy == 7):
                            temp[row+dy][col+dx] = "blackKing"
                        else:
                            temp[row+dy][col+dx] = temp[row][col]
                        temp[row][col] = None
                        temp[row+(dy//2)][col+(dx//2)] = None

                        moves.append(minString)
                        moreMoves = Game.blackCapturesFromSquare(temp, row+dy, col+dx)
                        for m in moreMoves:
                            moves.append(minString + "," + m)
        return moves


    @staticmethod
    def blackMovesFromSquare(board, row, col):

        if(board[row][col] == "blackKing"):
            Ys = [-1, 1]
            piece = "B"
        else:
            Ys = [1] #Only down
            piece = "b"

        moves = []
        for dx in [-1, 1]:
            for dy in Ys:
                if(Game.onBoard(row+dy, col+dx)):
                    if(row+dy == 0):
                        p = "B"
                    else:
                        p = piece
                    if(board[row+dy][col+dx] == None):
                        moves.append("-"+piece+str(row)+str(col)+",+" \
                                +p+str(row+dy)+str(col+dx))

        moves.extend(Game.blackCapturesFromSquare(board, row, col))
        return moves


    def movesRed(self):
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                square = self.board[row][col]
                if square and square.startswith("red"):
                    moves.extend(Game.redMovesFromSquare(self.board, row, col))

        return moves


    def movesBlack(self):
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                square = self.board[row][col]
                if square and square.startswith("black"):
                    moves.extend(Game.blackMovesFromSquare(self.board, row, col))

        return moves

    def moves(self):
        if(self.currPlayer == "black"):
            return self.movesBlack()
        else:
            return self.movesRed()

    def makeMove(self, moveString):
        moves = moveString.split(",")
        for move in moves:
            row = int(move[2])
            col = int(move[3])
            if(move[0] == "-"):
                if(move[1] == "b" or move[1] == "B"):
                    if(not self.board[row][col].startswith("black")):
                        print("poorly formed move: ", end="")
                        print(moveString)
                    self.board[row][col] = None
                elif(move[1] == "r" or move[1] == "R"):
                    if(not self.board[row][col].startswith("red")):
                        print("poorly formed move: ", end="")
                        print(moveString)
                    self.board[row][col] = None
            elif(move[0] == "+"):
                if(self.board[row][col] != None):
                    print("poorly formed move: ", end="")
                    print(moveString)
                if(move[1] == "r"):
                    self.board[row][col]="red"
                elif(move[1] == "R"):
                    self.board[row][col]="redKing"
                elif(move[1] == "b"):
                    self.board[row][col]="black"
                elif(move[1] == "B"):
                    self.board[row][col]="blackKing"




    def boardString(self):
        result = ""
        for row in self.board:
            for col in row:
                c = col
                if(c == "X"):
                    result += "[ ]"
                elif(c == None):
                    result += "[ ]"
                elif(c == "red"):
                    result += "[r]"
                elif(c == "redKing"):
                    result += "[R]"
                elif(c == "black"):
                    result += "[b]"
                elif(c == "blackKing"):
                    result += "[B]"
            result += "\n"
        return result
















