import heapq
from collections import defaultdict

with open('input.txt') as f:
    data = f.read().split()


def find_start():
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'S':
                return i, j


CHANGE_COST = 1000
MOVE_COST = 1
DIRECTIONS = (0, 1), (-1, 0), (0, -1), (1, 0)
NUM_DIRECTIONS = len(DIRECTIONS)


def solve(find_all=False):
    x, y = find_start()
    paths = defaultdict(list)
    direction = 0
    queue = [(0, x, y, direction, [])]
    seen = set()

    while queue:
        cost, x, y, direction, path = heapq.heappop(queue)

        if data[x][y] == '#':
            continue
        if data[x][y] == 'E':
            if not find_all:
                return cost
            paths[cost].append(path + [(x, y)])

        seen.add((x, y, direction))

        dirs = [
            (cost + MOVE_COST, x + DIRECTIONS[direction][0], y + DIRECTIONS[direction][1], direction, path + [(x, y)]),
            (cost + CHANGE_COST, x, y, (direction - 1) % NUM_DIRECTIONS, path),
            (cost + CHANGE_COST, x, y, (direction + 1) % NUM_DIRECTIONS, path)
        ]

        for d in dirs:
            key = d[1:-1]
            if key not in seen:
                if not find_all:  # insane optimizations
                    seen.add(key)
                heapq.heappush(queue, d)

    return len({p for path in paths[min(paths)] for p in path})


# ~1.05s
print(f'part 1: {solve()}')
print(f'part 2: {solve(find_all=True)}')
