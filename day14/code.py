#!/usr/bin/env python3

"""https://adventofcode.com/2022/day/#"""
import os,sys
from pathlib import Path
__author__ = "Chris Choy"

example = Path(os.getcwd()) / "example.txt"
problem = Path(os.getcwd()) / "input.txt"
assert(example.exists())
assert(problem.exists())

class Solution:
    def __init__(self, input, verbose=False):
        self.log = lambda s: print(s) if verbose else None
        self.src = []
        with open(input,'r') as input:
            for l in input.readlines():
                self.src.append(l.strip())

    def part1(self):
        pass 

    def part2(self):
        pass

#####
print(Solution(example).part1())
# print(Solution(problem).part1())