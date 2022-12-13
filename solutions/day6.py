import csv

def parse_input():
    with open('../inputs/day6.input', newline='') as csvfile:
        for row in csv.reader(csvfile): 
            return row[0]

def first_distinct_k(k):
    message = parse_input()
    for i in range(len(message)-k):
        if len(set(message[i:i+k])) == k:
            return i+k

def part_one():
    return first_distinct_k(4)
    
def part_two():
    return first_distinct_k(14)

print(part_one())
print(part_two())