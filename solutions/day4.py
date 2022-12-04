
import csv

def parse_input():
    with open('../inputs/day4.input', newline='') as csvfile:
        for row in csv.reader(csvfile): 
            row = ([tuple([int(y) for y in x.split('-')]) for x in row])
            yield row

def interval_covers(s1, e1, s2, e2):
    return (s1 >= s2 and e1 <= e2) or (s2 >= s1 and e2 <= e1)

def interval_overlap(s1, e1, s2, e2):
    return e2 >= s1 >= s2 or e2 >= e1 >= s2 or e1 >= s2 >= s1 or e1 >= e2 >= s1

def part_one():
    return sum(interval_covers(s1, e1, s2, e2) for (s1, e1), (s2, e2) in parse_input())

def part_two():
    return sum(interval_overlap(s1, e1, s2, e2) for (s1, e1), (s2, e2) in parse_input())


print(part_one())
print(part_two())
