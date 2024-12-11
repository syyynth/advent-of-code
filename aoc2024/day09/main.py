import heapq
from collections import defaultdict

with open('input.txt') as f:
    data = f.read().strip()


def unpack():
    unpacked = []
    counter = 0
    is_file = True

    for d in map(int, data):
        if is_file:
            unpacked.extend([counter] * d)
            counter += 1
        else:
            unpacked.extend([-1] * d)
        is_file ^= True

    return unpacked


def get_distances_and_positions(unpacked):
    distances = defaultdict(list)
    positions = defaultdict(list)

    start = True
    pos = 0
    for idx, n in enumerate(unpacked):
        if n != -1:
            if not start:
                heapq.heappush(distances[idx - pos], pos)
                start = True
            positions[n].append(idx)
        elif n == -1 and start:
            pos = idx
            start = False
    return distances, positions


def find_best_distance(distances, l):
    best_distance = float('inf')
    best_index = float('inf')

    for dist, heap in distances.items():
        if dist >= l and heap:
            candidate = heap[0]
            if candidate < best_index:
                best_distance = dist
                best_index = candidate

    return best_distance


def part1():
    unpacked = unpack()
    ans = 0

    left = 0
    right = len(unpacked) - 1
    while left < right:
        if unpacked[left] == -1 and unpacked[right] != -1:
            unpacked[left], unpacked[right] = unpacked[right], unpacked[left]
        while unpacked[left] != -1:
            left += 1
        while unpacked[right] == -1:
            right -= 1

    for idx, d in enumerate(unpacked):
        if d == -1:
            break

        ans += idx * d

    return ans


def part2():
    unpacked = unpack()
    distances, positions = get_distances_and_positions(unpacked)
    start = max(unpacked)

    while start > 0:
        file_positions = positions[start]
        file_length = len(file_positions)
        dist = find_best_distance(distances, file_length)

        if dist != float('inf'):
            pos_idx = heapq.heappop(distances[dist])
            if pos_idx < file_positions[0]:
                for shift, n in enumerate(file_positions):
                    unpacked[pos_idx + shift] = start
                    unpacked[n] = -1

                remaining = dist - file_length
                if remaining > 0:
                    heapq.heappush(distances[remaining], pos_idx + file_length)
        start -= 1

    return sum(
        idx * d
        for idx, d in enumerate(unpacked)
        if d != -1
    )


# ~0.07s
print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
