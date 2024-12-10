from collections import defaultdict

with open('input.txt') as f:
    data = f.read().split()


def in_bound(a, b):
    return 0 <= a < len(data) and 0 <= b < len(data[0])


def find_antennas():
    antennas_pos = defaultdict(list)

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != '.':
                antennas_pos[data[i][j]].append((i, j))

    return antennas_pos


def part1():
    antennas_pos = find_antennas()
    unique_antinodes = set()

    for freq, positions in antennas_pos.items():
        n = len(positions)

        for i in range(n):
            x1, y1 = positions[i]
            # start i + 1 to avoid duplicate pairs
            for j in range(i + 1, n):
                x2, y2 = positions[j]

                dx = x1 - x2
                dy = y1 - y2

                first = x1 + dx, y1 + dy
                second = x2 - dx, y2 - dy

                if in_bound(*first):
                    unique_antinodes.add(first)
                if in_bound(*second):
                    unique_antinodes.add(second)

    return len(unique_antinodes)


def part2():
    antennas_pos = find_antennas()
    unique_antinodes = set()

    for freq, positions in antennas_pos.items():
        n = len(positions)

        for i in range(n):
            x1, y1 = positions[i]
            for j in range(i + 1, n):
                x2, y2 = positions[j]

                dx = x2 - x1
                dy = y2 - y1

                # because field is a square, move along the slope
                for k in range(len(data)):
                    first = x1 + k * dx, y1 + k * dy
                    second = x2 - k * dx, y2 - k * dy

                    if in_bound(*first):
                        unique_antinodes.add(first)
                    if in_bound(*second):
                        unique_antinodes.add(second)

    return len(unique_antinodes)


print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
