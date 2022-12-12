#!/usr/bin/env python3

"""https://adventofcode.com/2022/day/6"""
import sys
__author__ = "Chris Choy"

assert(len(sys.argv) == 2) # python3 dN.py input.txt

BUFFSIZE = 14

def checkvalid(l):
    return len(set(l)) == BUFFSIZE

with open(sys.argv[1],'r') as f:
    for l in f.readlines():
        l = l.strip()
        buffer = []
        i = 0
        for c in l:
            i += 1
            buffer.append(c)
            if len(buffer) == BUFFSIZE:
                if checkvalid(buffer):
                    break 
                else:
                    buffer = buffer[1:]
    print("ANS:",i)