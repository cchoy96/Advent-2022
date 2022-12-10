#!/usr/bin/env python3

"""https://adventofcode.com/2022/day/11"""
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
    ans = []

    def answer(self):
        with open(self.f,'r') as f:
            for l in f.readlines():
                pass

        return None

#####
print(Solution(example).answer() == None)
print(Solution(problem).answer())