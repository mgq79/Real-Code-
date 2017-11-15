#!/usr/bin/env python

import random, sys

shake = false
if(len(sys.argv) > 1):
    shake = true



while(true):
    crit = false
    rollString = input()
    parts = rollString.split(' ')
    totalRoll = 0

