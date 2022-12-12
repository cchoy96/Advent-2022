#!/usr/bin/env python3

""" https://adventofcode.com/2022/day/2 """
import os,sys,pathlib
__author__ = "Chris Choy"

shape_pts = {'X': 1,'Y': 2,'Z': 3}
outcome_pts = {
    ('A','X'): 3, # rock
    ('B','Y'): 3, # paper
    ('C','Z'): 3, # scissors
    ('A','Y'): 6,
    ('B','Z'): 6,
    ('C','X'): 6,
    ('A','Z'): 0,
    ('B','X'): 0,
    ('C','Y'): 0,
}

with open("input.txt", 'r') as f:
    score = 0
    for line in f.readlines():
        op, me = line.strip().split(' ')
        round_score = shape_pts[me] + outcome_pts[(op,me)]
        score += round_score
    print("Part 1:", score)

outcome_pts = {'X':0,'Y':3,'Z':6}
shape_pts = {
    ('A','X'): 3, # lose to rock = scissors = 3 pts
    ('B','Y'): 2, # draw to paper = paper = 2 pts
    ('C','Z'): 1, # win against scissors = rock = 1 pt
    ('A','Y'): 1,
    ('B','Z'): 3,
    ('C','X'): 2,
    ('A','Z'): 2,
    ('B','X'): 1,
    ('C','Y'): 3,
}

with open("input.txt", 'r') as f:
    score = 0
    for line in f.readlines():
        op, outcome = line.strip().split(' ')
        round_score = shape_pts[(op,outcome)] + outcome_pts[outcome]
        score += round_score
    print("Part 2:", score)