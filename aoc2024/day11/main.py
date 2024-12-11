with open('input.txt') as f:
    data = [int(s) for s in f.read().strip().split()]

cache = {}


def decompose(stone, iterations):
    key = stone, iterations

    if key in cache:
        return cache[key]

    if iterations == 0:
        return 1

    if stone == 0:
        stones = [1]
    elif len(str(stone)) % 2 == 0:
        l = int(str(stone)[:len(str(stone)) // 2])
        r = int(str(stone)[len(str(stone)) // 2:])
        stones = [l, r]
    else:
        stones = [stone * 2024]

    cache[key] = sum(
        decompose(s, iterations - 1)
        for s in stones
    )
    return cache[key]


def solve(iterations):
    return sum(
        decompose(stone, iterations)
        for stone in data
    )


# ~0.21s
p1, p2 = solve(25), solve(75)
print(f'part 1: {p1}')
print(f'part 2: {p2}')
