#!/usr/bin/env python3

"""https://adventofcode.com/2022/day/12"""
import os,sys
from pathlib import Path
__author__ = "Chris Choy"

DEBUG = False
example = Path(os.getcwd()) / "example.txt"
problem = Path(os.getcwd()) / "input.txt"
assert(example.exists())
assert(problem.exists())

def myprint(s):
    if DEBUG: 
        print(s)

class Solution:
    def __init__(self,f):
        self.f = f
        self.grid = []
        with open(self.f,'r') as f:
            for l in f.readlines():
                self.grid.append([*l.strip()])
        self.max_steps = len(self.grid) * len(self.grid[0])

    def go(self, dir, row, col, visited):
        if dir == 'left':
            newr,newc = (row, col-1)
        elif dir == 'right':
            newr,newc = (row, col+1)
        elif dir == 'up':
            newr,newc = (row-1, col)
        elif dir == 'down':
            newr,newc = (row+1, col)
        try:
            if col < 0 or row < 0:
                return None
            curr_elev = ord(self.grid[row][col])
            next = self.grid[newr][newc]
            next_elev = ord(next if next != 'E' else 'z')
            if curr_elev + 1 < next_elev:
                myprint(dir, "too high")
                return None
            elif curr_elev > next_elev:
                myprint(dir, "too low")
                return None
            elif (newr, newc) in visited:
                myprint(dir, "already visited")
                return None
            else:
                return (newr, newc)
        except:
            return None

    def walk(self, curr, steps, visited, path):
        '''recursive function'''
        if steps >= self.max_steps:
            return self.max_steps
        elif curr == None:
            return self.max_steps
        print(steps, path, self.grid[curr[0]][curr[1]])
        if self.grid[curr[0]][curr[1]] == 'E':
            print("MADE IT!", steps,path)
            return steps
        else:
            l = self.go('left', *curr, visited)
            r = self.go('right', *curr, visited)
            u = self.go('up', *curr, visited)
            d = self.go('down', *curr, visited)
            return min(
                self.walk(l, steps+1, set(list(visited) + [l]), path+'<'),
                self.walk(r, steps+1, set(list(visited) + [r]), path+'>'),
                self.walk(u, steps+1, set(list(visited) + [u]), path+'^'),
                self.walk(d, steps+1, set(list(visited) + [d]), path+'v'),
            )

    def answer(self):
        min_steps = min(
            self.walk((0,1), 1, {(0,1)}, ">"), 
            self.walk((1,0), 1, {(1,0)}, "v")
        )
        return min_steps

#####
print(Solution(example).answer() == 31)
print(Solution(problem).answer())