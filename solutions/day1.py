import csv

def parse_input():
    with open('../inputs/day1.input', newline='') as csvfile:
        for row in csv.reader(csvfile): yield row

def elves():
    elves, current_food = [], 0
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
    return sum(sorted(elves())[-3:])

print(part_one())
print(part_two())
