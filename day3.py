import csv

def parse_input():
    with open('inputs/day3.input', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader: yield row[0]

def by_3(it):
    items = list(it)
    for pos in range(0, len(items), 3): yield items[pos:pos+3]

def priority(item):
    if 65 <= ord(item) <= 90: return ord(item) - 38
    return ord(item) - 96

def common(rucksack):
    N = int(len(rucksack) / 2)
    return min(set(rucksack[0:N]) & set(rucksack[N:]))

def common_three(rucksacks):
    first, second, third = rucksacks
    return min(set(first) & set(second) & set(third))

def part_1():
    return sum(priority(common(rucksack)) for rucksack in parse_input())

def part_2():
    return sum(priority(common_three(rucksacks)) for rucksacks in by_3(parse_input()))

print(part_2())