#!/usr/bin/env python3

"""https://adventofcode.com/2022/day/12"""
import os,sys,collections
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

    def get_val(self, node):
        return self.grid[node[0]][node[1]]

    def get_children(self, node):
        def go(dir, row, col):
            if dir == 'left':
                newr,newc = (row, col-1)
            elif dir == 'right':
                newr,newc = (row, col+1)
            elif dir == 'up':
                newr,newc = (row-1, col)
            elif dir == 'down':
                newr,newc = (row+1, col)
            
            if newr < 0 or newr >= len(self.grid) \
                or newc < 0 or newc >= len(self.grid[0]):
                return None 
            else:
                return (newr, newc)
                
        children = list(filter(None, [
            go('right', *node),
            go('down', *node),
            go('up', *node),
            go('left', *node),
        ]))
        return children

    def dist_from(self, start):
        visited, queue = set(), collections.deque([(start, 0)])

        while queue:
            curr_node, dist = queue.popleft()
            
            if curr_node in visited:
                continue
            else:
                visited.add(curr_node)
            
            if self.get_val(curr_node) == 'E':
                return dist

            for child in self.get_children(curr_node):
                if child not in visited:
                    curr_val = self.get_val(curr_node)
                    curr_elev = ord(curr_val) if curr_val != 'S' else ord('a')
                    child_val = self.get_val(child)
                    child_elev = ord(child_val) if child_val != 'E' else ord('z')

                    if curr_elev + 1 >= child_elev:
                        # visited.add(child)
                        queue.append((child, dist+1))
        return self.max_steps

    def answer(self, part):
        # part1
        if part == 1:
            for rowi,row in enumerate(self.grid):
                for coli,val in enumerate(row):
                    if val == 'S':
                        return self.dist_from((rowi, coli))
        
        # part2
        if part == 2:
            dists = []
            for rowi,row in enumerate(self.grid):
                for coli,val in enumerate(row):
                    if val == 'a':
                        dists.append(self.dist_from((rowi,coli)))
            return min(dists)

#####
print(Solution(example).answer(1) == 31)
print(Solution(example).answer(2) == 29)
print(Solution(problem).answer(1) == 472)
print(Solution(problem).answer(2) == 465)