#!/usr/bin/env python3

"""https://adventofcode.com/2022/day/8"""
import sys
__author__ = "Chris Choy"

assert(len(sys.argv) == 2) # python3 dN.py input.txt

grid = []

with open(sys.argv[1],'r') as f:
    for l in f.readlines():
        l = l.strip()
        grid.append([int(c) for c in l])

def visiblefromleft(rowitems,col,height):
    vis = True
    score = 0
    for tree in rowitems[:col]:
        if tree >= height:
            vis = False
            score = 1
        else:
            score += 1
    score = 1 if score == 0 else score
    return (vis,score)
def visiblefromright(rowitems,col,height):
    vis = True
    score = 0
    for tree in rowitems[col+1:]:
        score += 1
        if tree >= height:
            vis = False
            break
    return (vis,score)
def visiblefromtop(row,col,height):
    aboverows = grid[:row]
    vis = True
    score = 0
    for rowitems in aboverows:
        if rowitems[col] >= height:
            vis = False
            score = 1
        else:
            score += 1
    score = 1 if score == 0 else score
    return (vis,score)
def visiblefrombottom(row,col,height):
    belowrows = grid[row+1:]
    vis = True
    score = 0
    for rowitems in belowrows:
        score += 1
        if rowitems[col] >= height:
            vis = False
            break
    score = 1 if score == 0 else score
    return (vis,score)

num_visible = 0
scores = []
for row,rowitems in enumerate(grid):
    # print(rowitems)
    for col,height in enumerate(rowitems):
        visible = False
        if row == 0 or row == (len(grid) - 1) or col == 0 or col == (len(rowitems) - 1): # on edge
            visible = True
        elif visiblefromtop(row,col,height) or visiblefrombottom(row,col,height):
            visible = True
        elif visiblefromleft(rowitems,col,height) or visiblefromright(rowitems,col,height):
            visible = True
        
        if visible:
            num_visible += 1
    for col,height in enumerate(rowitems):
        s1 = visiblefromtop(row,col,height)[1]
        s2 = visiblefromleft(rowitems,col,height)[1]
        s3 = visiblefromright(rowitems,col,height)[1]
        s4 = visiblefrombottom(row,col,height)[1]
        score = s1*s2*s3*s4
        # print(s1,s2,s3,s4,"=",score)
        scores.append(s1*s2*s3*s4)
# print(num_visible)
print(max(scores))