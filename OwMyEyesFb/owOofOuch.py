#!/usr/bin/env python

import sys, string

if(len(sys.argv) < 2):
    print("You need an argument")
    exit()

msg = sys.argv[1:]
msg = " ".join(msg)
print(msg)

result = ""
for i in range(len(msg)):
    if(msg[i] in string.whitespace):
        result += msg[i]
    elif(i % 2 == 0):
        result += "_"+msg[i]+"_"
    else:
        result += "*"+msg[i]+"*"

print(result)
