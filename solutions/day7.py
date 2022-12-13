from __future__ import annotations
from dataclasses import dataclass
import csv

def parse_input():
    with open('../inputs/day7.input', newline='') as csvfile:
        for row in csv.reader(csvfile): 
            yield row[0]

@dataclass
class Node:
    name: str
    children: Dict[str, set[Node]]
    parent: Node
    weight: int

class TreeManager:
    def __init__(self, root):
        self.root = root
        self.cur = root
    
    def ls(self, command):
        for item in command:
            if item[0:3] == "dir":
                dirname = item[3:].strip()
                new_node = Node(f"{self.cur.name}/{dirname}", {}, self.cur, 0)
                self.cur.children[dirname] = new_node
            else:
                size, filename = item.split()
                self.cur.weight += int(size)

    def cd(self, command):
        newdir = command[0][2:].strip()
        if newdir == "..":
            self.cur = self.cur.parent
        else:
            self.cur = self.cur.children[newdir]

class CommandParser:
    def __init__(self, input_stream):
        self.commands = self.parse_commands(input_stream)
        self.tree = TreeManager(root=Node("/", {}, None, 0))
        self.final_weights = {}

    def parse_commands(self, input_stream):
        commands = []
        cur = [next(input_stream)[2:]]

        for idx, item in enumerate(input_stream):
            if item[0] == "$":
                commands.append(cur)
                cur = [item[2:]]
            else:
                cur.append(item)
        
        commands.append(cur)
        return commands

    def run_commands(self):
        for command in self.commands:
            self.execute(command)
    
    def execute(self, command):
        if command[0][0:2] == "ls":
            self.tree.ls(command[1:])

        if command[0][0:2] == "cd":
            self.tree.cd(command)

    def determine_weights_recursively(self, val):
        new_weight = val.weight
        for child in val.children.values():
            new_weight += self.determine_weights_recursively(child)
        
        self.final_weights[val.name] = new_weight
        return new_weight

def part_one():
    parser = CommandParser(parse_input())
    parser.run_commands()
    parser.determine_weights_recursively(parser.tree.root)
    return sum(v for v in parser.final_weights.values() if v <= 100000)

def part_two():
    parser = CommandParser(parse_input())
    parser.run_commands()
    parser.determine_weights_recursively(parser.tree.root)
    total_space = 70000000
    total_used = parser.final_weights['/']

    return sorted([v for v in parser.final_weights.values() if v > 30000000 - (total_space - total_used)])[0]
        

print(part_one())
print(part_two())