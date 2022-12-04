#!/usr/bin/env python3

"""https://adventofcode.com/2022/day/4"""
import os,sys,pathlib
__author__ = "Chris Choy"

assert(len(sys.argv) == 2) # python3 dN.py input.txt

with open(sys.argv[1],'r') as f:
    count = 0
    for l in f.readlines():
        l = l.strip()
    print("Part1:",count)
