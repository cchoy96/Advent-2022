#!/usr/bin/env python

"""https://adventofcode.com/2022/day/1"""
import os,sys,pathlib
__author__ = "Chris Choy"

elves = [0]

with open("input.txt",'r') as f:
    elfi = 0
    for line in f.readlines():
        if line.strip() == "":
            elfi += 1
            elves.append(0)
        else:
            elves[elfi] += int(line.strip())

print("Part 1: {}".format(max(elves)))
print("Part 2: {}".format(sum(sorted(elves)[-3:])))
