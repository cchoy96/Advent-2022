#!/usr/bin/env python3

"""https://adventofcode.com/2022/day/9"""
import os,sys
from pathlib import Path
__author__ = "Chris Choy"

assert(len(sys.argv) == 2) # python3 dN.py input.txt

visited = set()
def follows(hpos, tpos):
    hx,hy = hpos 
    tx,ty = tpos
    xdist = abs(hx-tx)
    ydist = abs(hy-ty)
    return xdist > 1 or ydist > 1

def move(pos, dir):
    x,y = pos 
    if dir == 'L':
        x-=1
    elif dir == 'R':
        x+=1
    elif dir == 'U':
        y+=1
    elif dir == 'D':
        y-=1
    return (x,y)

with open(sys.argv[1],'r') as f:
    rope = [(0,0)] * 10 # H,1,2,...,9
    visited.add(rope[-1])
    for l in f.readlines():
        dir, steps = l.strip().split(' ')
        print("===={} {}====".format(dir,steps))
        for _ in range(int(steps)):
            rope[0] = move(rope[0],dir)
            for i in range(1,len(rope)):
                if follows(rope[i-1],rope[i]):
                    x1,y1 = rope[i-1]
                    x2,y2 = rope[i]
                    if x2 < x1:
                        x2 += 1
                    if x2 > x1:
                        x2 -= 1
                    if y2 < y1:
                        y2 += 1
                    if y2 > y1:
                        y2 -= 1
                    rope[i] = (x2,y2)
            visited.add(rope[-1])
            print(rope)
    print("ANS:", len(visited))
