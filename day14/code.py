#!/usr/bin/env python3

"""https://adventofcode.com/2022/day/#"""
import os,sys,time
from pathlib import Path
__author__ = "Chris Choy"

example = Path(os.getcwd()) / "example.txt"
problem = Path(os.getcwd()) / "input.txt"
assert(example.exists())
assert(problem.exists())

class Solution:
    def __init__(self, input, verbose=False):
        self.verbose = verbose
        self.log = lambda s: print(s) if verbose else None
        self.src = []
        x_min, x_max = 600, 0
        y_rng = 0
        with open(input,'r') as input:
            for l in input.readlines():
                line = []
                for coord in l.strip().split(" -> "):
                    x,y = coord.split(',')
                    x_min = min(x_min, int(x))
                    x_max = max(x_max, int(x))
                    y_rng = max(y_rng, int(y))
                    line.append((int(x), int(y)))
                self.src.append(line)
        
        for i in range(len(self.src)): # crop x values
            for j in range(len(self.src[i])):
                x,y = self.src[i][j]
                self.src[i][j] = (x-x_min, y)
        self.origin = (500-x_min, 0)
        
        self.grid = [['.' for x in range (x_max-x_min+1)] for y in range(y_rng + 1)]
        for line in self.src:
            px, py = None, None 
            for tx,ty in line:
                self.grid[ty][tx] = '#'
                if px:
                    for x,y in self.connect(px,py,tx,ty):
                        self.grid[y][x] = '#'
                px,py = tx,ty

    def printmap(self, key='&', crop=None):
        print(key,' '.join([str(i) for i in range(len(self.grid[0]))]))
        grid = self.grid[crop[0]:crop[1]] if crop else self.grid
        for i,line in enumerate(grid):
            print(i, ' '.join(line),)
        print('\n')

    def connect(self, xa,ya, xb,yb):
        if xa == xb:
            return [(xa,y) for y in range(min(ya,yb), max(ya,yb))]
        elif ya == yb:
            return [(x,ya) for x in range(min(xa,xb), max(xa,xb))]
        else:
            print("ERROR connecting lines for ({},{}) to ({},{})".format(xa,ya,xb,yb))
    
    def drop(self):
        def fall(x,y):
            if y+1 >= len(self.grid):
                return None # falls down into abyss
            if self.grid[y+1][x] == '.':
                return (x,y+1) # Drop down
            if x-1 < 0:
                return None # falls left into abyss
            elif self.grid[y+1][x-1] == '.':
                return (x-1,y+1) # Drop left
            if x+1 >= len(self.grid[0]):
                return None # falls right into abyss 
            elif self.grid[y+1][x+1] == '.':
                return (x+1,y+1)
            return (x,y) # at rest  
        
        old_pos = self.origin 
        while (pos := fall(*old_pos)) != None:
            if pos == old_pos:
                break
            else:
                old_pos = pos # keep falling
        return pos

    def part1(self):
        counter = 0
        while (final_pos := self.drop()):
            counter += 1
            x,y = final_pos
            self.grid[y][x] = 'o'

            if self.verbose:
                self.printmap(counter)

                if counter > 630:
                    x = input("Hit enter to step:")
                if counter > 1000: 
                    break
        return counter

    def part2(self):
        pass

#####
# print(Solution(example).part1() == 24)
print(Solution(problem,verbose=True).part1())
print(Solution(problem).part1())
