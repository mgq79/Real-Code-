

from tkinter import *

# Card class should contain
# - the type of card (color, shape, fill, count)
# - given a canvas and coordinates (and maybe size)
#    it should be able to draw itself
# - Contain the frame of animation it's on for the card flip


class Card(object):
    color_choices = ['red', 'green', 'purple']
    shape_choices = ['diamond', 'oblong', 'squiggle']
    count_choices =  [1, 2, 3]
    fill_choices  = ['solid', 'lined', 'empty']
        #For lined, see stipple option and bitmaps,
        #either custom or gray12 or 25 maybe

    def __init__(this, color, shape, count, fill):
        this.color = color_choices[color]
        this.shape = shape_choices[shape]
        this.count = count_choices[count]
        this.fill  = fill_choices[fill]

        this.animFrame = 0


    def drawDiamond(this, canvas, x0, y0, x1, y1):
        point1 = ((x0+y0)/2, y0) # Top
        point2 = (x1, (y0+y1)/2) # Right
        point3 = ((x0+y0)/2, y1) # Bottom
        point4 = (x0, (y0+y1)/2) # Left

        if(this.fill == 'solid'):
            canvas.create_polygon(point1, point2, point3, point4,
                    color=this.color, fill=this.color)
        elif(this.fill == 'empty'):
            canvas.create_polygon(point1, point2, point3, point4,
                    color=this.color, fill='')
        elif(this.fill == 'lined'):
            canvas.create_polygon(point1, point2, point3, point4,
                    color=this.color, fill=this.color, stipple='gray25')

    def drawOblong(this, canvas, x0, y0, x1, y1):
        if(this.fill == 'solid'):
            canvas.create_oval(x0, y0, x1, y1,
                    color=this.color, fill=this.color)
        elif(this.fill == 'empty'):
            canvas.create_oval(x0, y0, x1, y1,
                    color=this.color, fill='')
        elif(this.fill == 'lined'):
            canvas.create_polygon(point1, point2, point3, point4,
                    color=this.color, fill=this.color, stipple='gray25')

    def drawSquiggle(this, canvas, x0, y0, x1, y1):
        hSpace = (x1-x0)/3
        vSpace = (y1-y0)/2

        p1 = (x0 + 0*hSpace, y0 + 1*vSpace)
        p2 = (x0 + 1*hSpace, y0 + 0*vSpace)
        p3 = (x0 + 2*hSpace, y0 + 1*vSpace)
        p4 = (x0 + 3*hSpace, y0 + 0*vSpace)
        p5 = (x0 + 3*hSpace, y0 + 1*vSpace)
        p6 = (x0 + 2*hSpace, y0 + 0*vSpace)
        p7 = (x0 + 1*hSpace, y0 + 1*vSpace)
        p8 = (x0 + 0*hSpace, y0 + 0*vSpace)

        if(this.fill == 'solid'):
            canvas.create_polygon(p1, p2, p3, p4, p5, p6, p7, p8,
                    color=this.color, fill=this.color)
        elif(this.fill == 'empty'):
            canvas.create_polygon(p1, p2, p3, p4, p5, p6, p7, p8,
                    color=this.color, fill='')
        elif(this.fill == 'lined'):
            canvas.create_polygon(p1, p2, p3, p4, p5, p6, p7, p8,
                    color=this.color, fill=this.color, stipple='gray25')

    def draw(this, canvas, x0, y0, x1, y1):

