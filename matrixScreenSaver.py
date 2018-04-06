#!/usr/bin/env python3

import random, time

def matString(l, prevString=None):
    if(prevString == None):
        x = ""
        for i in range(l):
            z = random.randrange(0,10)
            if(z == 0):
                x += "0"
            elif(z == 1):
                x += "1"
            else:
                x += " "
        return x
    else:
        assert(l == len(prevString))
        x = ""
        for i in range(l):
            z = -1
            if(prevString[i] != " "):
                z = random.randrange(0,4)
            elif(prevString[max(0, i-1)] != " " or prevString[min(l-1, i+1)] != " "):
                z = random.randrange(0, 8)
            else:
                z = random.randrange(0,200)

            if(z == 0):
                m = "matt"[random.randrange(4)]
                x += "0"
            elif(z == 1):
                x += "1"
            else:
                x += " "
        return x


def matLoop(d):
    p = None
    while(True):
        p = matString(d, p)
        print(p)
        time.sleep(0.1)

matLoop(150)
