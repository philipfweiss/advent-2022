import csv
import numpy as np

def parse_input():
    mtx = None
    with open('../inputs/day8_small.input', newline='') as csvfile:
        for idx, row in enumerate(csv.reader(csvfile)): 
            if idx == 0:
                N = len(row[0])
                mtx = np.zeros((N, N))
            
            mtx[idx, :] = np.array([int(v) for v in row[0]])
    return mtx, N

def part_one():
    rot, N = parse_input()
    visible_trees = np.zeros((N, N))

    visible = (4*N - 4)
    for _ in range(4):
        rot = np.rot90(rot)
        visible_trees = np.rot90(visible_trees)
        M, N = rot.shape

        for i in range(1, M-1):
            max_so_far = rot[i, 0]
            for j in range(1, N-1):
                if rot[i, j] > max_so_far:
                    max_so_far = rot[i, j]
                    visible_trees[i, j] = 1

    return visible + np.sum(visible_trees)

def part_two():
    rot, N = parse_input()
    visible_trees = np.ones((N, N))

    for _ in range(1):
        # rot = np.rot90(rot)
        visible_trees = np.rot90(visible_trees)
        M, N = rot.shape

        for i in range(M):
            max_so_far = rot[i, 0]
            for j in range(N):
                if rot[i, j] > max_so_far:
                    max_so_far = rot[i, j]
                    visible_trees[i, j] *= j
    print(rot)
    print(visible_trees)

    return np.max(visible_trees)


print(part_two())
