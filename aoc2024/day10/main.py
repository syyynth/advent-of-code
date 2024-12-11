with open('input.txt') as f:
    data = f.read().split()

DIRECTIONS = (-1, 0), (1, 0), (0, -1), (0, 1)


def in_bound(x, y):
    return 0 <= x < len(data) and 0 <= y < len(data[0])


def get_zeros():
    return [
        (int(i), int(j))
        for i in range(len(data))
        for j in range(len(data[i]))
        if data[i][j] == '0'
    ]


def is_full_trail(x, y):
    return int(data[x][y]) == 9


def explore(x, y, c, start):
    score_data = set()
    rating = 0

    if not in_bound(x, y) or int(data[x][y]) != c:
        return score_data, rating

    if is_full_trail(x, y):
        return {(start, (x, y))}, 1

    for dx, dy in DIRECTIONS:
        score_data_partial, rating_partial = explore(x + dx, y + dy, c + 1, start)
        score_data |= score_data_partial
        rating += rating_partial

    return score_data, rating


def solve():
    zeros = get_zeros()

    score_data = set()
    rating = 0

    for x, y in zeros:
        for dx, dy in DIRECTIONS:
            score_data_partial, rating_partial = explore(x + dx, y + dy, 1, (x, y))
            score_data |= score_data_partial
            rating += rating_partial

    return len(score_data), rating


p1, p2 = solve()

# ~0.017s
print(f'part 1: {p1}')
print(f'part 2: {p2}')
