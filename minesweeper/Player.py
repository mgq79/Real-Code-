
from tkinter import *
from Board import Board

def init(data):
    data.rows = 15
    data.cols = 18
    data.board = Board(data.rows, data.cols)
    data.nMines = 22
    data.board.placeMines(data.nMines)
    data.board.placeNumbers()

    data.margin = 25
    data.cellSize = min((data.width  - 2*data.margin)/data.cols,
                        (data.height - 2*data.margin)/data.rows)



def drawCell(canvas, data, row, col):
    top = data.margin + data.cellSize * row
    left = data.margin + data.cellSize * col
    bottom = data.margin + data.cellSize * (row+1)
    right  = data.margin + data.cellSize * (col+1)

    cellVal = data.board.board[row][col]
    cellCenter = (left + data.cellSize/2, top + data.cellSize/2)

    if(not data.board.revealed[row][col]):
        canvas.create_rectangle(left, top, right, bottom, fill='darkgrey', width = 1)
        if(data.board.marked[row][col]):
            canvas.create_text(cellCenter, text="X")
    else:
        canvas.create_rectangle(left, top, right, bottom, fill='lightgrey', width = 1)

        if(cellVal != 0):
            canvas.create_text(cellCenter, text=str(cellVal))


def drawGrid(canvas, data):
    for row in range(data.rows):
        for col in range(data.cols):
            drawCell(canvas, data, row, col)

def redrawAll(canvas, data):
    drawGrid(canvas, data)
    if(data.board.checkWin()):
        canvas.create_text(data.width//2, 10, text="You Win!")

def mousePressed(event, data, isRight=False):
    x = event.x - data.margin
    y = event.y - data.margin
    col = int(x//data.cellSize)
    row = int(y//data.cellSize)

    if(0 <= row and row < data.rows and
       0 <= col and col < data.cols):
        if(isRight):
            if(not data.board.revealed[row][col]):
                data.board.marked[row][col] = not data.board.marked[row][col]
        else:
            data.board.reveal(row, col)



def keyPressed(event, data):
    if(event.keysym == "r"):
        init(data)

def timerFired(data):
    pass

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data, isRight=False):
        mousePressed(event, data, isRight)
        redrawAllWrapper(canvas, data)

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
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Button-2>", lambda event:
                            mousePressedWrapper(event, canvas, data, True))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed


run(500, 400)
