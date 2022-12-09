#!/usr/bin/env python3

"""https://adventofcode.com/2022/day/#"""
import os,sys
from pathlib import Path
__author__ = "Chris Choy"

assert(len(sys.argv) == 2) # python3 dN.py input.txt

visited = set()
def tailmoves(hpos, tpos):
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
    hpos = (0,0)
    tpos = (0,0)
    visited.add(tpos)
    for l in f.readlines():
        dir, steps = l.strip().split(' ')
        # print("===={} {}====".format(dir,steps))
        for _ in range(int(steps)):
            hpos = move(hpos,dir)
            if tailmoves(hpos,tpos):
                hx,hy = hpos
                tx,ty = tpos 
                if tx < hx:
                    tpos = move(tpos,'R')
                if tx > hx:
                    tpos = move(tpos,'L')
                if ty < hy:
                    tpos = move(tpos,'U')
                if ty > hy:
                    tpos = move(tpos,'D')
            visited.add(tpos)
            # print(hpos,tpos)
    print("ANS:", len(visited))
