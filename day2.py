# First column: opponent's move (A, B, C)
# Second column: what to play in response

# Total score: sum of scores for each round
# A -> 1, B -> 2, C -> 3 + Outcome (0, 3, 6)
from ast import parse
import csv

def parse_input():
    with open('inputs/day2.input', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            yield row

def round_score(first, second):
    points = { 'X': 1, 'Y': 2, 'Z': 3 }
    outcomes = {
        ('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
        ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
        ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
    }

    return points[second] + outcomes[(first, second)]

def round_2_score(first, second):
    win = { 'A': 'Y', 'B': 'Z', 'C': 'X'}
    draw = { 'A': 'X', 'B': 'Y', 'C': 'Z'}
    lose = { 'A': 'Z', 'B': 'X', 'C': 'Y'}
    guide = {
        'X': lose,
        'Y': draw,
        'Z': win,
    }
    return round_score(first, guide[second][first])

def part_one():
    return sum(round_score(*rnd) for rnd in parse_input())

def part_two():
    return sum(round_2_score(*rnd) for rnd in parse_input())

