
from SnakeGame import SnakeBoard
from tkinter import *


def init(data):
    data.rows = 15
    data.cols = 15
    data.maxDelay = 400
    data.minDelay = 80
    data.lastDirection = (0, 0)
    data.timerDelay = data.maxDelay
    data.game = SnakeBoard(data.rows, data.cols)

    data.margin = 25
    data.cellSize = min((data.width  - 2*data.margin)/data.cols,
                        (data.height - 2*data.margin)/data.rows)


def drawCell(canvas, data, row, col):
    top = data.margin + data.cellSize * row
    left = data.margin + data.cellSize * col
    bottom = data.margin + data.cellSize * (row+1)
    right  = data.margin + data.cellSize * (col+1)

    cellCenter = (left + data.cellSize/2, top + data.cellSize/2)

    if(data.game.isBody(row, col)):
        canvas.create_rectangle(left, top, right, bottom, fill='green', width = 1)
    elif(data.game.isFood(row, col)):
        canvas.create_rectangle(left, top, right, bottom, fill='blue', width = 1)
    else:
        canvas.create_rectangle(left, top, right, bottom, fill='lightgrey', width =      1)

def drawGrid(canvas, data):
    for row in range(data.rows):
        for col in range(data.cols):
            drawCell(canvas, data, row, col)

def keyPressed(event, data):
    if(event.keysym == 'Down'):
        if(not data.lastDirection == (-1, 0)):
            data.game.direction = (1, 0)
    elif(event.keysym == 'Right'):
        if(not data.lastDirection == (0, -1)):
            data.game.direction = (0, 1)
    elif(event.keysym == 'Up'):
        if(not data.lastDirection == (1, 0)):
            data.game.direction = (-1, 0)
    elif(event.keysym == 'Left'):
        if(not data.lastDirection == (0, 1)):
            data.game.direction = (0, -1)
    elif(event.keysym == 'r'):
        init(data)

def timerFired(data):
    data.game.stepBoard()
    data.timerDelay = data.maxDelay - 10*(data.game.snakeLen - 3)
    data.timerDelay = max(data.timerDelay, data.minDelay)
    data.lastDirection = data.game.direction

def redrawAll(canvas, data):
    drawGrid(canvas, data)
    if(data.game.gameOver):
        canvas.create_text(data.width//2, 10, text="Game Over!")



def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed



run(500, 400)
