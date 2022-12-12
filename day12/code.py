#!/usr/bin/env python3

"""https://adventofcode.com/2022/day/#"""
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
        self.src = []
        with open(self.f,'r') as f:
            for l in f.readlines():
                self.src.append(l.strip())

    def answer(self):
        
        return None

#####
print(Solution(example).answer() == None)
# print(Solution(problem).answer())