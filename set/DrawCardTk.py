#!/usr/bin/env python3

from tkinter import *
from Card import Card


root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()

Card(0, 0, 0, 2).setBoundingBox(10, 10, 90, 130).flipUp().draw(canvas)
Card(0, 0, 1, 2).setBoundingBox(100, 10, 180, 130).flipUp().draw(canvas)
Card(0, 0, 2, 2).setBoundingBox(190, 10, 270, 130).flipUp().draw(canvas)
Card(0, 1, 0, 0).setBoundingBox(280, 10, 360, 130).flipUp().draw(canvas)
Card(0, 2, 0, 0).setBoundingBox(370, 10, 450, 130).flipUp().draw(canvas)

canvas.update









if(__name__ == "__main__"):
    root.mainloop()
