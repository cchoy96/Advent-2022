#!/usr/bin/env python3

"""https://adventofcode.com/2022/day/11"""
import os,sys,operator,math
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
OPS = {
    '+' : operator.add,
    '*' : operator.mul,
}

class Monkey:
    def __init__(self, src):
        # Monkey ID
        self.id = int(src[0].split(' ')[1].strip(':'))
        # Starting items
        self.items = [int(x) for x in src[1].split(': ')[1].split(', ')]
        # Operation
        oper,val = src[2].split(' ')[-2:]
        if val == "old":
            self.inspect = lambda x: OPS[oper](x,x)
        else:
            self.inspect = lambda x: OPS[oper](x,int(val))
        # Test
        self.divby = int(src[3].split(' ')[-1])
        t1 = int(src[4].split(' ')[-1])
        t2 = int(src[5].split(' ')[-1])
        self.throw = lambda x: t1 if (x % self.divby) == 0 else t2

        self.inspected = 0
        self.lcm = 1

    def set_lcm(self, lcm):
        self.lcm = lcm

    def takeTurn(self):
        thrown = []
        while len(self.items) != 0:
            item = self.items.pop(0)
            # worry = int(self.inspect(item) / 3) # part 1
            worry = int(self.inspect(item) % self.lcm) # part 2
            self.inspected += 1
            target = self.throw(worry)
            thrown.append((target, worry))
        return thrown

    def giveItem(self, val):
        self.items.append(val)
    
    def __str__(self):
        s = "Monkey {}:\n".format(self.id)
        s += "\tItems: {}\n".format(self.items)
        s += "\tOp: new = old [+*] {}\n".format(self.inspect(1))
        s += "\tTest: throw to monkey {} if divisible by X else monkey {}"\
            .format(self.throw(0), self.throw(1))
        return s
    
    def held(self):
        return "Monkey {}: {}".format(self.id, self.items)

class Solution:
    def __init__(self,f):
        monkeys_src = [[]]
        with open(f,'r') as f:
            for l in f.readlines():
                l = l.strip()
                if l == "":
                    monkeys_src.append([])
                else:
                    monkeys_src[-1].append(l)
        
        self.monkeys = []
        divs = []
        for src in monkeys_src:
            m = Monkey(src)
            self.monkeys.append(m)
            divs.append(m.divby)
            # print(self.monkeys[-1])
        
        lcm = math.lcm(*divs)
        for m in self.monkeys:
            m.set_lcm(lcm)

    def answer(self):
        for round in range(10_000):
            print(round)
            for monkey in self.monkeys:
                # print(monkey.id, monkey.items)
                thrown = monkey.takeTurn()
                # print(monkey.id, thrown)
                for target,worry in thrown:
                    self.monkeys[target].giveItem(worry)
            # print([m.held() for m in self.monkeys])
        
        inspected = [m.inspected for m in self.monkeys]
        most = max(inspected)
        inspected.remove(most)
        second_most = max(inspected)
        return most * second_most

#####
# print(Solution(example).answer() == 10605)
print(Solution(example).answer() == 2713310158)
print(Solution(problem).answer())