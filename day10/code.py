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

def solution(f):
    ans = []
    with open(f,'r') as f:
        for l in f.readlines():
            pass
    return ans


#####
assert(solution(example) == _)
# print(solution(problem))