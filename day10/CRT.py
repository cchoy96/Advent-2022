#!/usr/bin/env python3

"""https://adventofcode.com/2022/day/10"""
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

class Solution():
    def __init__(self, f):
        self.f = f
        self.cycle = 0
        self.x = 1
        self.vals = []
        self.grid = ""

    def run_cycle(self):
        if self.cycle in [40,80,120,160,200,240]:
            self.grid += '\n'
        c = '#' if self.cycle%40 in range(self.x-1, self.x+2) else '.'
        self.grid += c

        self.cycle += 1
        if self.cycle in [20,60,100,140,180,220]:
            self.vals.append(self.x * self.cycle)

    def answer(self):
        with open(self.f,'r') as f:
            for l in f.readlines():
                toks = l.strip().split(' ')
                if toks[0] == "noop":
                    self.run_cycle()
                elif toks[0] == "addx":
                    val = int(toks[1])
                    for _ in range(2):
                        self.run_cycle()
                    self.x += val
                # if self.cycle > 40:
                #     break
        print(self.grid)
        return sum(self.vals)

#####

print(Solution(example).answer() == 13140)
print(Solution(problem).answer() == 10760)