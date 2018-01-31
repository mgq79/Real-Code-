#!/usr/bin/env python

from tkinter import *
import math, time

def init(data):
    data.timerDelay       = 1
    data.hourRadius       = 180
    data.minuteRadius     = 215
    data.secondRadius     = 200
    data.hourTickLength   = 30
    data.minuteTickLength = 8
    data.maxRadius        = 230
    data.hourTickColor    = 'lightgrey'
    data.minuteTickColor  = 'lightgrey'
    data.hourTickWidth    = 3
    data.minuteTickWidth  = 2
    data.triColor         = 'cyan'
    data.hourPoint        = None
    data.minutePoint      = None
    data.secondPoint      = None
    data.lerpRate         = 0.5

def pointOnCircle(data, radius, angle):
    centerX = data.width/2
    centerY = data.height/2
    y = radius*math.sin(angle) + centerY
    x = radius*math.cos(angle) + centerX
    return (x,y)


def lerp(point0, point1, rate):
    (x0, y0) = point0
    (x1, y1) = point1
    return (x0*rate + x1*(1-rate),y0*rate + y1*(1-rate))

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

def drawClockTriangle(canvas, data):
    hour = int(time.strftime("%I"))
    minute = int(time.strftime("%M"))
    second = int(time.strftime("%S"))

    hourAngle = (hour-3)*math.pi/6
    minuteAngle = (minute-15)*math.pi/30
    secondAngle = (second-15)*math.pi/30

    if(data.hourPoint == None):
        data.hourPoint   = pointOnCircle(data, data.hourRadius, hourAngle)
        data.minutePoint = pointOnCircle(data, data.minuteRadius, minuteAngle)
        data.secondPoint = pointOnCircle(data, data.secondRadius, secondAngle)


    data.hourPoint = lerp(data.hourPoint, pointOnCircle(data, data.hourRadius, hourAngle), data.lerpRate)
    data.minutePoint = lerp(data.minutePoint, pointOnCircle(data, data.minuteRadius, minuteAngle), data.lerpRate)
    data.secondPoint = lerp(data.secondPoint, pointOnCircle(data, data.secondRadius, secondAngle), data.lerpRate)

    (xh, yh) = data.hourPoint
    (xm, ym) = data.minutePoint
    (xs, ys) = data.secondPoint

    canvas.create_line(xh, yh, xm, ym, fill=data.triColor)
    canvas.create_line(xh, yh, xs, ys, fill=data.triColor)
    canvas.create_line(xm, ym, xs, ys, fill=data.triColor)



def redrawAll(canvas, data):
    drawClockFace(canvas,data)
    drawClockTriangle(canvas, data)

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

run(600, 500)
