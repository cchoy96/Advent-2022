#!/usr/bin/env python3

"""https://adventofcode.com/2022/day/4"""
import os,sys,pathlib
__author__ = "Chris Choy"

assert(len(sys.argv) == 2) # python3 dN.py input.txt

test = [
    list("ZN"),
    list("MCD"),
    list("P")
]

input = [
    list("HTZD"),
    list("QRWTGCS"),
    list("PBFQNRCH"),
    list("LCNFHZ"),
    list("GLFQS"),
    list("VPWZBRCS"),
    list("ZFJ"),
    list("DLVZRHQ"),
    list("BHGNFZLD"),
]

cargo = test
cargo = input

def parse(line):
    toks = line.split(' ')
    amt = int(toks[1])
    src = int(toks[3]) - 1
    dst = int(toks[5]) - 1
    return (amt,src,dst)

def answer(list):
    s = ""
    for l in list:
        s += l[-1]
    return s

with open(sys.argv[1],'r') as f:
    for l in f.readlines():
        amt,src,dst = parse(l.strip())
        crates = cargo[src][-amt:]
        # crates.reverse() # comment out for part 2
        cargo[src] = cargo[src][:-amt]
        cargo[dst].extend(crates)
    print("ANS:",answer(cargo))