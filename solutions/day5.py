import csv
import re

def parse_input():
    with open('../inputs/day5.input', newline='') as csvfile:
        for row in csv.reader(csvfile): 
            matches = re.search("move (\d+) from (\d+) to (\d+)", row[0])
            yield int(matches.group(1)), int(matches.group(2)), int(matches.group(3))

class Stack:
    def __init__(self, state):
        self.state = state

    def push(self, item):
        self.state.append(item)
    
    def pop(self):
        return self.state.pop(-1) if self.state else ""
    
    def peek(self):
        return self.state[-1] if self.state else ""

class Crates:
    def __init__(self, stacks):
        self.stacks = [Stack(list(stack)) for stack in stacks]

    def move(self, amount, from_crate, to_crate):
        for _ in range(amount):
            item = self.stacks[from_crate-1].pop()
            self.stacks[to_crate-1].push(item)

    def move_chunk(self, amount, from_crate, to_crate):
        buffer = [self.stacks[from_crate-1].pop() for _ in range(amount)]
        for item in reversed(buffer):
            self.stacks[to_crate-1].push(item)
    
    def display(self):
        return "".join(stack.peek() for stack in self.stacks)

def solve(by_chunk):
    crates = Crates(["BPNQHDRT", "WGBJTV", "NRHDSVMQ", "PZNMC", "DZB", "VCWZ", "GZNCVQLS", "LGJMDNV", "TPMFZCG"])
    for values in parse_input():
        crates.move_chunk(*values) if by_chunk else crates.move(*values)

    return crates.display()

def part_one():
    return solve(by_chunk=False)

def part_two():
    return solve(by_chunk=True)

print(part_one())
print(part_two())