#!/usr/bin/env python3

"""https://adventofcode.com/2022/day/13"""
import os,sys,collections
from pathlib import Path
__author__ = "Chris Choy"

example = Path(os.getcwd()) / "example.txt"
problem = Path(os.getcwd()) / "input.txt"
assert(example.exists())
assert(problem.exists())

DEBUG = False
def myprint(s):
    if DEBUG: 
        print(s)

class Solution:
    def __init__(self,f):
        src = []
        with open(f,'r') as f:
            for l in f.readlines():
                src.append(l.strip())
        
        self.pairs = []
        self.packetlist = []
        for i in range(0,len(src),3):
            left = self.parse_packet(src[i])
            right = self.parse_packet(src[i+1])
            self.pairs.append((left,right))
            self.packetlist.append(left)
            self.packetlist.append(right)
    
    def parse_packet(self, s):
        s = s[1:-1]
        stack = []
        buffer = []
        for c in s:
            # print(c, stack)
            if c.isdigit():
                buffer.append(c) # handles issues with double digit values
            elif c == ',':
                if buffer != []:
                    stack.append(int(''.join(buffer)))
                    buffer = []
            elif c == '[':
                stack.append(c)
            if c == ']':
                if buffer != []:
                    stack.append(int(''.join(buffer)))
                    buffer = []

                new_list = collections.deque()
                while stack:
                    item = stack.pop()
                    if item == '[':
                        stack.append(list(new_list))
                        break
                    else:
                        new_list.appendleft(item)
        if buffer != []:
            stack.append(int(''.join(buffer)))
        return list(stack)
    
    def difference(self, left, right):
        # Negative value for ordered, Positive for not ordered, 0 for equal
        myprint("\tcompare {} and {}".format(left,right))
        match left, right:
            case int(), int():
                return left - right
            case int(), list():
                return self.difference([left], right)
            case list(), int():
                return self.difference(left, [right])
            case list(), list():
                for l, r in zip(left, right):
                    if (diff := self.difference(l, r)) > 0:
                        return diff
                return len(left) - len(right)
    
    def answer(self):
        ordered = []
        for i, packets in enumerate(self.pairs):
            if self.difference(*packets) < 0:
                ordered.append(i+1) # 1 indexed
        myprint(ordered)
        return sum(ordered)

    def answer2(self):
        from functools import cmp_to_key
        self.packetlist.append([[2]])
        self.packetlist.append([[6]])

        sp = sorted(self.packetlist, key=cmp_to_key(self.difference))
        ans = []
        for i,val in enumerate(sp):
            if val == [[2]]:
                ans.append(i+1)
            elif val == [[6]]:
                ans.append(i+1)
                break 
        return ans[0]*ans[1]



#####
print(Solution(example).answer()==13)
print(Solution(problem).answer()==5580)
print(Solution(example).answer2()==140)
print(Solution(problem).answer2()==26200)