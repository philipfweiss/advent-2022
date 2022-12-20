import csv
from dataclasses import dataclass

@dataclass
class Position:
    x: int
    y: int

class RopePhysics:
    def __init__(self, num_knots):
        self.knots = [
            Position(0, 0) for _ in range(num_knots)
        ]
        self.num_knots = num_knots
        self.tail_positions = {(0, 0)}

    def move(self, movement, amount):
        for _ in range(int(amount)):
            if movement == 'U':
                self.knots[0].y += 1
            if movement == "D":
                self.knots[0].y -= 1
            if movement == "R":
                self.knots[0].x += 1
            if movement == "L":
                self.knots[0].x -= 1
            
            for i in range(self.num_knots - 1):
                self.tail_movement(i, i+1)

    def tail_movement(self, i, j):
        # Is the tail 2 steps away from the head?
        if (self.knots[i].x == self.knots[j].x) and self.knots[i].y == self.knots[j].y - 2: # Tail on top
            self.knots[j].y -= 1
        elif (self.knots[i].x == self.knots[j].x) and self.knots[i].y == self.knots[j].y + 2: # Tail below
            self.knots[j].y += 1
        elif (self.knots[i].y == self.knots[j].y) and self.knots[i].x == self.knots[j].x - 2: # Tail to the right
            self.knots[j].x -= 1
        elif (self.knots[i].y == self.knots[j].y) and self.knots[i].x == self.knots[j].x + 2:  # Tail to the left
            self.knots[j].x += 1

         # Is the tail 2 steps away from the head?
        elif abs(self.knots[i].x - self.knots[j].x) >= 1 and self.knots[i].y == self.knots[j].y - 2: # Tail on top
            self.knots[j].y -= 1
            if self.knots[j].x > self.knots[i].x:
                self.knots[j].x -= 1
            else:
                self.knots[j].x += 1
        elif abs(self.knots[i].x - self.knots[j].x) >= 1 and self.knots[i].y == self.knots[j].y + 2: # Tail below
            self.knots[j].y += 1
            if self.knots[j].x > self.knots[i].x:
                self.knots[j].x -= 1
            else:
                self.knots[j].x += 1
        elif abs(self.knots[i].y - self.knots[j].y) >= 1 and self.knots[i].x == self.knots[j].x - 2: # Tail to the right
            self.knots[j].x -= 1
            if self.knots[j].y > self.knots[i].y:
                self.knots[j].y -= 1
            else:
                self.knots[j].y += 1
        elif abs(self.knots[i].y - self.knots[j].y) >= 1 and self.knots[i].x == self.knots[j].x + 2: # Tail to the left
            self.knots[j].x += 1
            if self.knots[j].y > self.knots[i].y:
                self.knots[j].y -= 1
            else:
                self.knots[j].y += 1

        self.tail_positions.add((self.knots[-1].x, self.knots[-1].y))

def parse_input():
    with open('../inputs/day9.input', newline='') as csvfile:
        for row in csv.reader(csvfile): 
            yield row[0].split()

def part_one():
    rp = RopePhysics(2)
    for movement, amount in parse_input():
        rp.move(movement, amount)
    
    print(len(rp.tail_positions))

def part_two():
    rp = RopePhysics(10)
    for movement, amount in parse_input():
        rp.move(movement, amount)
    
    print(len(rp.tail_positions))

part_one()
part_two()
