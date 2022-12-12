#!/usr/bin/env python3

"""https://adventofcode.com/2022/day/3"""
import os,sys,pathlib
__author__ = "Chris Choy"

def tovalue(c):
    val = ord(c)
    if val > 96 and val < 123:
        val -= 96
    elif val > 64 and val < 91:
        val -= 38
    return val

assert(tovalue('a') == 1)
assert(tovalue('z') == 26)
assert(tovalue('A') == 27)
assert(tovalue('Z') == 52)

def get_duplicate(s1,s2):
    for c in s1:
        for d in s2:
            if c == d:
                return c
    print("ERR: no duplicate item found!")

with open("input.txt",'r') as f:
    psum = 0
    for l in f.readlines():
        l = l.strip()
        half = int(len(l) / 2)
        dupe = get_duplicate(l[:half], l[half:])
        val = tovalue(dupe)
        psum += tovalue(dupe)
    print("Part1:", psum)


def get_badge(elves):
    for i in elves[0]:
            for j in elves[1]:
                for k in elves[2]:
                    if i == j and i == k:
                        return i
    print("ERROR: no badge found!")

with open("input.txt",'r') as f:
    psum = 0
    while True:
        elves = ['','','']
        line = f.readline()
        if line == "":
            break 
        elves[0] = line 
        elves[1] = f.readline()
        elves[2] = f.readline()
        b = get_badge(elves)
        psum += tovalue(b)
    print("Part2:", psum)


