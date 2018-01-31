#!/usr/bin/env python

from tkinter import *
import math

def init(data):
    data.hourRadius   = 75
    data.minuteRadius = 90
    data.secondRadius = 85
    data.hourTickLength = 30
    data.minuteTickLength = 8
    data.maxRadius = 230
    data.hourTickColor = 'lightgrey'
    data.minuteTickColor = 'lightgrey'
    data.hourTickWidth = 3
    data.minuteTickWidth = 2
    data.triColor = 'cyan'

def pointOnCircle(data, radius, angle):
    centerX = data.width/2
    centerY = data.height/2
    y = radius*math.sin(angle) + centerY
    x = radius*math.cos(angle) + centerX
    return (x,y)

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def drawClockFace(canvas, data):
    centerX = data.width/2
    centerY = data.height/2

    minuteTicks = True
    if(minuteTicks):
        for i in range(60):
            angle = math.pi*i/30
            radius0 = data.maxRadius
            radius1 = data.maxRadius - data.minuteTickLength
            (x0, y0) = pointOnCircle(data, radius0, angle)
            (x1, y1) = pointOnCircle(data, radius1, angle)
            canvas.create_line(x0, y0, x1, y1, fill=data.minuteTickColor, width=data.minuteTickWidth)

    #Always do hour ticks
    for i in range(12):
        angle = math.pi*i/6
        radius0 = data.maxRadius
        radius1 = data.maxRadius - data.hourTickLength
        (x0, y0) = pointOnCircle(data, radius0, angle)
        (x1, y1) = pointOnCircle(data, radius1, angle)
        canvas.create_line(x0, y0, x1, y1, fill=data.hourTickColor, width=data.hourTickWidth)



def redrawAll(canvas, data):
    drawClockFace(canvas,data)

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
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
    #init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # initialize:
    init(data)
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600, 500)
