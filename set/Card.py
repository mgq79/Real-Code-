from tkinter import *

# Card class should contain
# - the type of card (color, shape, fill, count)
# - given a canvas and coordinates (and maybe size)
#    it should be able to draw itself
# - Contain the frame of animation it's on for the card flip
class Card(object):
        #For lined, see stipple option and bitmaps,
        #either custom or gray12 or 25 maybe

    def __init__(this, color, shape, count, fill):
        color_choices = ['red', 'green', 'purple']
        shape_choices = ['diamond', 'oblong', 'squiggle']
        count_choices =  [1, 2, 3]
        fill_choices  = ['solid', 'lined', 'empty']
        this.color = color_choices[color]
        this.shape = shape_choices[shape]
        this.count = count_choices[count]
        this.fill  = fill_choices[fill]
        this.animFrame = 0

    @staticmethod
    def isSet(card1, card2, card3):
        colorSet = set()
        colorSet.add(card1.color)
        colorSet.add(card2.color)
        colorSet.add(card3.color)
        if(len(colorSet) != 1 or len(colorSet) != 3):
            return False

        shapeSet = set()
        shapeSet.add(card1.shape)
        shapeSet.add(card2.shape)
        shapeSet.add(card3.shape)
        if(len(shapeSet) != 1 or len(shapeSet) != 3):
            return False

        countSet = set()
        countSet.add(card1.count)
        countSet.add(card2.count)
        countSet.add(card3.count)
        if(len(countSet) != 1 or len(countSet) != 3):
            return False

        fillSet = set()
        fillSet.add(card1.fill)
        fillSet.add(card2.fill)
        fillSet.add(card3.fill)
        if(len(fillSet) != 1 or len(fillSet) != 3):
            return False

        return True

    def drawDiamond(this, canvas, x0, y0, x1, y1):
        point1 = ((x0+x1)/2, y0) # Top
        point2 = (x1, (y0+y1)/2) # Right
        point3 = ((x0+x1)/2, y1) # Bottom
        point4 = (x0, (y0+y1)/2) # Left

        if(this.fill == 'solid'):
            canvas.create_polygon(point1, point2, point3, point4,
                    fill=this.color)
        elif(this.fill == 'empty'):
            canvas.create_polygon(point1, point2, point3, point4,
                    fill=this.color)
        elif(this.fill == 'lined'):
            canvas.create_polygon(point1, point2, point3, point4,
                    fill=this.color)

    def drawOblong(this, canvas, x0, y0, x1, y1):
        if(this.fill == 'solid'):
            canvas.create_oval(x0, y0, x1, y1,
                    fill=this.color)
        elif(this.fill == 'empty'):
            canvas.create_oval(x0, y0, x1, y1,
                    fill=this.color)
        elif(this.fill == 'lined'):
            canvas.create_oval(x0, y0, x1, y1,
                    fill=this.color)

    def drawSquiggle(this, canvas, x0, y0, x1, y1):
        hSpace = (x1-x0)/3
        vSpace = (y1-y0)/2

        p1 = (x0 + 0*hSpace, y0 + 1*vSpace)
        p2 = (x0 + 1*hSpace, y0 + 0*vSpace)
        p3 = (x0 + 2*hSpace, y0 + 1*vSpace)
        p4 = (x0 + 3*hSpace, y0 + 0*vSpace)
        p5 = (x0 + 3*hSpace, y0 + 1*vSpace)
        p6 = (x0 + 2*hSpace, y0 + 2*vSpace)
        p7 = (x0 + 1*hSpace, y0 + 1*vSpace)
        p8 = (x0 + 0*hSpace, y0 + 2*vSpace)

        if(this.fill == 'solid'):
            canvas.create_polygon(p1, p2, p3, p4, p5, p6, p7, p8,
                    fill=this.color)
        elif(this.fill == 'empty'):
            canvas.create_polygon(p1, p2, p3, p4, p5, p6, p7, p8,
                    fill=this.color)
        elif(this.fill == 'lined'):
            canvas.create_polygon(p1, p2, p3, p4, p5, p6, p7, p8,
                    fill=this.color)

    def drawShape(this, canvas, x0, y0, x1, y1):
        if(this.shape == "diamond"):
            this.drawDiamond(canvas, x0, y0, x1, y1)
        elif(this.shape == "oblong"):
            this.drawOblong(canvas, x0, y0, x1, y1)
        elif(this.shape == "squiggle"):
            this.drawSquiggle(canvas, x0, y0, x1, y1)
        else:
            print("invalid shape: " + this.shape)
            exit(1)

    def draw(this, canvas, x0, y0, x1, y1):
        width  = x1-x0
        height = y1-y0
        bLeft = x0 + width/4
        bRight = x0 + width*3/4
        bTop = y0 + height/3
        bBottom = y0 + height*2/3
        bPadding = (bBottom-bTop)/6 # This 6 might have to adjust

        canvas.create_rectangle(x0, y0, x1, y1)
        if(this.count == 1):
            this.drawShape(canvas, bLeft, bTop, bRight, bBottom)
