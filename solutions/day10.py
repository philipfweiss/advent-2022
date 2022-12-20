import csv
import numpy as np

class InstructionManager:
    def __init__(self):
        self.cycle_count = 1
        self.register = 1
        self.pending = {}
        self.signal = 0
        self.grid = np.zeros((6, 40))

    def noop(self):
        self.cycle_count += 1
        self.add_signal()
        self.draw()

    def addx(self, V):
        self.noop()
        self.register += int(V)
        self.noop()

    def add_signal(self):
        if self.cycle_count % 40 == 20:
            self.signal += self.cycle_count * self.register

    def draw(self):
        pixelno = (self.cycle_count % 40) - 1
        row = (self.cycle_count - 1) // 40
        if abs(self.register - pixelno) < 2:
            self.grid[row, pixelno] = 1
    
    def display(self):
        for i in range(6):
            line = ""
            for j in range(40):
                line += "#" if self.grid[i, j] == 1 else " "
            yield line

def parse_input():
    with open('../inputs/day10.input', newline='') as csvfile:
        for row in csv.reader(csvfile): 
            yield row[0].split()

def run():
    im = InstructionManager()
    for instruction in parse_input():
        if instruction[0] == 'addx':
            im.addx(instruction[1])
        else:
            im.noop()
    return im

def part_one():
    print(run().signal)

def part_two():
    for line in run().display():
        print(line)

part_one()
part_two()