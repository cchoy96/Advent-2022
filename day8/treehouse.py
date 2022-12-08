#!/usr/bin/env python3

"""https://adventofcode.com/2022/day/8"""
import os,sys
from pathlib import Path
__author__ = "Chris Choy"

def isvisible(trees, height):
    for tree in trees:
        if tree >= height:
            return False 
    return True 

def getscore(trees, height):
    score = 0
    for tree in trees[::-1]: # go from inside to out
        score += 1
        if tree >= height:
            break 
    return score

def main(fp):
    grid = []
    with open(fp,'r') as f:
        for l in f.readlines():
            l = l.strip()
            grid.append([int(c) for c in l])

    num_visible = 0
    scores = []
    for rowi, row in enumerate(grid):
        for coli, height in enumerate(row):
            # lists go from perimeter trees in
            l = row[:coli]
            r = row[coli+1:][::-1]
            u = [r[coli] for r in grid[:rowi]]
            d = [r[coli] for r in grid[rowi+1:]][::-1]

            for tree_list in [u,l,r,d]:
                if isvisible(tree_list, height):
                    num_visible += 1
                    break
            
            score = 1
            for tree_list in [u,l,r,d]:
                score *= getscore(tree_list, height)
            scores.append(score)

    return (num_visible, max(scores))

testfile = Path(os.getcwd()) / "test.txt"
inputfile = Path(os.getcwd()) / "input.txt"
assert(testfile.exists())
assert(inputfile.exists())

assert(main(testfile) == (21,8))
print(main(inputfile))
