#!/usr/bin/env python3

"""https://adventofcode.com/2022/day/4"""
import os,sys,pathlib
__author__ = "Chris Choy"

assert(len(sys.argv) == 2) # python3 dN.py input.txt

with open(sys.argv[1],'r') as f:
    count = 0
    for l in f.readlines():
        a,b = l.strip().split(',')
        a1,a2 = a.split('-')
        b1,b2 = b.split('-')
        if int(a1) <= int(b1) and int(b2) <= int(a2):
            count += 1
        elif int(b1) <= int(a1) and int(a2) <= int(b2):
            count += 1
    print("Part1:",count)

with open(sys.argv[1],'r') as f:
    count = 0
    for l in f.readlines():
        a,b = l.strip().split(',')
        a1,a2 = a.split('-')
        b1,b2 = b.split('-')
        al = [*range(int(a1),int(a2)+1,1)]
        bl = [*range(int(b1),int(b2)+1,1)]
        for i in al:
            if i in bl:
                count += 1
                break
    print("Part2:",count)