from copy import deepcopy

with open('input.txt') as f:
    data = [list(line) for line in f.read().split()]


def find_loc(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in '^>v<':
                return i, j


def find_delta(direction):
    deltas = {
        '^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)
    }
    return deltas[direction]


def rotate_direction(direction):
    rotation = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    return rotation[direction]


def check_bounds(row, col, grid):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def is_obstacle(x, y, grid):
    return grid[x][y] == '#'


def part1():
    grid = deepcopy(data)
    row, col = find_loc(grid)
    visited = {(row, col)}

    while True:
        direction = grid[row][col]
        dx, dy = find_delta(direction)
        nrow, ncol = row + dx, col + dy

        if not check_bounds(nrow, ncol, grid):
            return visited
        if is_obstacle(nrow, ncol, grid):
            grid[row][col] = rotate_direction(direction)
        else:
            visited.add((nrow, ncol))
            grid[nrow][ncol], grid[row][col] = grid[row][col], '.'
            row, col = nrow, ncol


def part2():
    visited_positions = part1()
    initial_row, initial_col = find_loc(data)
    initial_direction = data[initial_row][initial_col]
    visited_positions.remove((initial_row, initial_col))

    count = 0
    for obstacle_row, obstacle_col in visited_positions:
        seen_states = set()
        data[obstacle_row][obstacle_col] = '#'

        row, col = initial_row, initial_col
        direction = initial_direction

        while True:
            dx, dy = find_delta(direction)
            nrow, ncol = row + dx, col + dy

            if not check_bounds(nrow, ncol, data):
                break
            if is_obstacle(nrow, ncol, data):
                direction = rotate_direction(direction)
            else:
                state = (nrow, ncol, direction)
                if state in seen_states:
                    count += 1
                    break
                seen_states.add(state)
                data[nrow][ncol], data[row][col] = direction, '.'
                row, col = nrow, ncol

        data[obstacle_row][obstacle_col] = '.'
        data[initial_row][initial_col] = initial_direction

    return count


print(f'part 1: {len(part1())}')
print(f'part 2: {part2()}')  # idk about 10 secs
