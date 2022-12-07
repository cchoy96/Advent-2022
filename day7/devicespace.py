#!/usr/bin/env python3

"""https://adventofcode.com/2022/day/7"""
import sys
from enum import Enum
__author__ = "Chris Choy"

assert(len(sys.argv) == 2) # python3 dN.py input.txt

def getpathstr(l):
    return "/".join(l)

# LType = Enum('LType', ["CD","LS","DIR","FILE"])
def process(s,path,read_paths):
    toks = s.split(' ')
    if s.startswith("$ cd"):
        dst = toks[2]
        if dst == "..":
            path.pop()
        else:
            path.append(dst)
            p = getpathstr(path)
            if p not in dirs:
                dirs[p] = 0
        # print(path)
    elif s.startswith("$ ls"):
        pass
    elif s.startswith("dir"):
        pass
    else: # files
        filepath = getpathstr(path + [toks[1]])
        if filepath not in read_paths:
            for i in range(len(path)):
                p = getpathstr(path[:i+1])
                dirs[p] += int(toks[0])
            read_paths.append(filepath)

path = [] # '/', 'a', 'b' = /a/b
dirs = {} # map of directory to total_size
read_paths = []

with open(sys.argv[1],'r') as f:
    for l in f.readlines():
        l = l.strip()
        process(l,path,read_paths)

    ans = 0
    for dir, total_size in dirs.items():
        if total_size < 100000:
            ans += total_size
    print("PART1:",ans)

# Part 2
needed = 30_000_000 - 70_000_000 + dirs["/"]
candidates = []
for dir,total_size in dirs.items():
    if total_size >= needed:
        candidates.append(total_size)
print("PART2:", min(candidates))