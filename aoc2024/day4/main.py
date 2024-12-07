with open('input.txt') as f:
    data = f.read().split()
    n = len(data)  # row
    m = len(data[0])  # col


def check_bounds(row, col):
    return 0 <= row < n and 0 <= col < m


def explore(row, col, dx, dy, word, target):
    if not check_bounds(row, col):
        return 0
    if data[row][col] == word[target]:
        if target == len(word) - 1:
            return 1
        return explore(row + dx, col + dy, dx, dy, word, target + 1)
    return 0


def part1():
    ans = 0
    word = 'XMAS'
    for row in range(n):
        for col in range(m):
            if data[row][col] == word[0]:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1),
                               (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    ans += explore(row + dx, col + dy, dx, dy, word, 1)
    return ans


def part2():
    ans = 0
    for row in range(n):
        for col in range(m):
            if data[row][col] == 'A':
                ans += 2 == sum(
                    explore(row + dx, col + dy, 0, 0, 'M', 0)
                    and explore(row - dx, col - dy, 0, 0, 'S', 0)
                    for dx, dy in [(1, 1), (1, -1), (-1, -1), (-1, 1)]
                )
    return ans


print(f'part1: {part1()}')
print(f'part2: {part2()}')
