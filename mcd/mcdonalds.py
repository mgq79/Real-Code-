# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.fries = []
    data.nstripes = 13
    data.stripeH = data.height/data.nstripes
    data.blueH = data.stripeH*(data.nstripes//2)
    filename = "frenchfry.gif"
    data.frypic = PhotoImage(file="frenchfry.gif")
    data.ballpic = PhotoImage(file="yf.gif")
    data.baseball = False
    data.balls = []
    data.all = []

def mousePressed(event, data):
    if data.baseball:
        data.all.append(((event.x, event.y), 'yf'))
        data.balls.append((event.x, event.y))
    else:
        data.all.append(((event.x, event.y), 'fry'))
        data.fries.append((event.x, event.y))

def keyPressed(event, data):
    if event.char=="u":
        if data.all != []:
            ((x, y), label) = data.all.pop()
            if(label == 'yf'):
                data.balls.pop()
            else:
                data.fries.pop()
        #if data.baseball:
        #    if data.balls!=[]:
        #        data.balls.pop()
        #else:
        #    if data.fries!=[]:
        #        data.fries.pop()
    if event.keysym == "space":
        data.baseball = not data.baseball

def timerFired(data):
    pass

def drawFlag(canvas, data):
    x0 = 0
    x1 = data.width
    y0 = 0
    y1 = data.stripeH
    for i in range (data.nstripes):
        if i%2 == 0:
            fill = "black"
        else:
            fill = "white"
        canvas.create_rectangle(x0, y0, x1, y1, fill=fill, width=0)
        y0 += data.stripeH
        y1 += data.stripeH
    canvas.create_rectangle(0, 0, data.width/2, data.blueH, fill="blue", width=0)

def drawFries(canvas, data):
    for (x, y) in data.fries:
        canvas.create_image(x, y, image=data.frypic)

def drawBalls(canvas, data):
    for (x, y) in data.balls:
        canvas.create_image(x, y, image=data.ballpic)

def drawAllImages(canvas, data):
    for ((x, y), label) in data.all:
        if(label == "yf"):
            canvas.create_image(x, y, image=data.ballpic)
        else:
            canvas.create_image(x, y, image=data.frypic)

def redrawAll(canvas, data):
    drawFlag(canvas, data)
    #drawFries(canvas, data)
    #drawBalls(canvas, data)
    drawAllImages(canvas, data)
    canvas.create_text(data.width-2, data.height-2,
                       anchor="se", text="click or press space!\npress u to undo",
                       font="Arial 12")

####################################
# use the run function as-is
####################################

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

run(1920, 1080)