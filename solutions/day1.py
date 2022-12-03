import csv
from itertools import groupby

def parse_input():
    with open('../inputs/day1.input', newline='') as csvfile:
        for row in csv.reader(csvfile): yield int(row[0]) if row else -1

def elves():
    return [sum(chunk) for is_chunk, chunk in groupby(parse_input(), key=lambda x: x>0) if is_chunk]

def part_one():
    return max(elves())

def part_two():
    return sum(sorted(elves())[-3:])

print(part_one())
print(part_two())
