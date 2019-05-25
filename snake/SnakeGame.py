
import random

class SnakeBoard(object):
    def __init__(this, rows, cols):
        this.rows = rows
        this.cols = cols
        this.board = [0] * this.rows
        # head to tail
        this.snake = [(1,2), (1,1), (1, 0)]
        this.snakeLen = 3
        # (dRow, dCol)
        this.direction = (0, 1)
        for i in range(this.rows):
            this.board[i] = [0] * cols
        for r, c in this.snake:
            this.board[r][c] = 1

        this.gameOver = False
        this.placeFood()

    def onBoard(this, row, col):
        return (0 <= row and row < this.rows and
                0 <= col and col < this.cols)

    def isBody(this, row, col):
        if(0 <= row and row < this.rows and
           0 <= col and col < this.cols):
            return (this.board[row][col] == 1)
        else:
            return None

    def isFood(this, row, col):
        if(0 <= row and row < this.rows and
           0 <= col and col < this.cols):
            return (this.board[row][col] == 2)
        else:
            return None

    def placeFood(this):
        validTiles = []
        for row in range(this.rows):
            for col in range(this.cols):
                if(not (this.isFood(row, col) or this.isBody(row, col))):
                    validTiles.append((row, col))
        if(len(validTiles) > 0):
            r, c = validTiles[random.randrange(len(validTiles))]
            this.board[r][c] = 2


    def stepBoard(this):
        if(this.gameOver):
            return
        curHeadRow, curHeadCol = this.snake[0]
        dRow, dCol = this.direction
        newRow, newCol = (curHeadRow + dRow, curHeadCol + dCol)
        if(not this.onBoard(newRow, newCol)):
            this.gameOver = True
            return
        if(this.isBody(newRow, newCol)):
            this.gameOver = True
            return
        if(this.isFood(newRow, newCol)):
            this.snakeLen += 1
            this.placeFood()

        for r, c in this.snake:
            this.board[r][c] = 0

        this.snake.insert(0, (newRow, newCol))
        this.snake = this.snake[:this.snakeLen]

        for r, c in this.snake:
            this.board[r][c] = 1



