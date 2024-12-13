import re

import numpy as np

with open('input.txt') as f:
    data = [
        list(map(int, re.findall(r'\d+', line)))
        for line in f.read().split('\n\n')
    ]


def solve(error):
    total = 0

    for ax, ay, bx, by, x, y in data:
        A = np.array([[ax, bx],
                      [ay, by]])
        b = np.array([x + error, y + error])

        x_rounded = np.round(np.linalg.lstsq(A, b)[0]).astype(int)

        if np.allclose(A @ x_rounded - b, 0):
            total += x_rounded[0] * 3 + x_rounded[1]

    return total


print(f'part 1: {solve(0)}')
print(f'part 2: {solve(10000000000000)}')
