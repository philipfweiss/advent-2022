import csv

def parse_input():
    with open('inputs/day1.input', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            yield row

def elves():
    elves = []
    current_food = 0
    for row in parse_input():
        if len(row) == 0:
            elves.append(current_food)
            current_food = 0
        else:
            current_food += int(row[0])
    return elves
    
def part_one():
    return max(elves())

def part_two():
    return sum(list(reversed(sorted(elves())))[0:3])

part_two()