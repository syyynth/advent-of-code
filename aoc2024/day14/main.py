import re
from copy import deepcopy
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

WIDE, TALL = 101, 103
IMG_DIR = Path('img')
IMG_DIR.mkdir(parents=True, exist_ok=True)

with open('input.txt') as f:
    data = {
        n: list(map(int, re.findall(r'-?\d+', line)))
        for n, line in enumerate(f)
    }
    field = [[0] * WIDE for _ in range(TALL)]
    for _, (x, y, *_) in data.items():
        field[y][x] += 1


def update_positions(data, field):
    for n, (x, y, vx, vy) in data.items():
        field[y][x] -= 1
        nx, ny = (x + vx) % WIDE, (y + vy) % TALL
        field[ny][nx] += 1
        data[n][:2] = [nx, ny]


def calculate_quadrants(field):
    q1 = q2 = q3 = q4 = 0
    mh = len(field) // 2
    mv = len(field[0]) // 2
    for i in range(len(field)):
        for j in range(len(field[i])):
            if i < mh and j < mv:
                q1 += field[i][j]
            if i < mh and j > mv:
                q2 += field[i][j]
            if i > mh and j < mv:
                q3 += field[i][j]
            if i > mh and j > mv:
                q4 += field[i][j]
    return q1 * q2 * q3 * q4


def save_to_png(field, sec):
    plt.imsave(
        IMG_DIR / f'sec_{sec}.png',
        (np.array(field) != 0).astype(int),
        cmap=ListedColormap(['black', 'orange'])
    )


def solve(steps, save_images=False):
    local_data, local_field = deepcopy(data), deepcopy(field)
    for sec in range(steps):
        if save_images:
            save_to_png(local_field, sec)
        update_positions(local_data, local_field)
    return calculate_quadrants(local_field)


print(f'Part 1: {solve(100)}')
solve(9000, save_images=True)
print('Part 2: Check images in the img folder and find the tree. Increase iterations if needed.')
