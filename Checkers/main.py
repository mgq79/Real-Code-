#!/usr/bin/env python3

from tkinter import *
from Game import Game

def init(data):
    data.game = Game()
    data.margin = int(0.05 * data.width)
    data.squareSide = int((0.9 * data.width)/8)

def pointToCoord(event, data):
    margin = data.margin
    squareSide = data.squareSide

    for row in range(8):
        for col in range(8):
            y1 = margin + row*squareSide
            x1 = margin + col*squareSide
            y2 = margin + (row+1)*squareSide
            x2 = margin + (col+1)*squareSide

            if( x1 <= event.x and event.x < x2 \
            and y1 <= event.y and event.y < y2):
                return (row, col)
    return (-1, -1)


def clickListener(event, data):
    pass

def keyListener(event, data):
    pass

def drawBoard(canvas, data):
    margin = data.margin
    squareSide = data.squareSide

    for row in range(8):
        for col in range(8):
            y1 = margin + row*squareSide
            x1 = margin + col*squareSide
            y2 = margin + (row+1)*squareSide
            x2 = margin + (col+1)*squareSide

            if((row+col)%2 == 0):
                fill = "white"
            else:
                fill = "black"

            canvas.create_rectangle(x1, y1, x2, y2, fill=fill)

            pad = 3
            if(data.game.board[row][col] == "red"):
                canvas.create_oval(x1+pad, y1+pad, x2-pad, y2-pad, fill="red")
            elif(data.game.board[row][col] == "black"):
                canvas.create_oval(x1+pad, y1+pad, x2-pad, y2-pad, fill="black")


def redrawAll(canvas, data):
    drawBoard(canvas, data)

def run(width, height):

    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()

    def clickWrapper(event, canvas, data):
        clickListener(event, data)
        redrawAllWrapper(canvas, data)

    def keypressWrapper(event, canvas, data):
        keyListener(event, data)
        redrawAllWrapper(canvas, data)

    class Struct(object): pass
    data = Struct()
    data.width  = width
    data.height = height

    #TODO init stuff
    init(data)

    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()

    root.bind("<Button-1>", lambda event:
                        clickWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                        keypressWrapper(event, canvas, data))

    redrawAllWrapper(canvas, data)
    root.mainloop()



if __name__ == "__main__":
    run(600,600)
