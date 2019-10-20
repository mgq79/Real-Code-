#!/usr/bin/env python3

from tkinter import *
from Card import Card


root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()

Card(0, 0, 0, 0).draw(canvas, 10, 10, 90, 130)
Card(0, 0, 0, 0).draw(canvas, 100, 10, 180, 130)
Card(0, 0, 0, 0).draw(canvas, 190, 10, 270, 130)
Card(0, 1, 0, 0).draw(canvas, 280, 10, 360, 130)
Card(0, 2, 0, 0).draw(canvas, 370, 10, 450, 130)

canvas.update









if(__name__ == "__main__"):
    root.mainloop()
