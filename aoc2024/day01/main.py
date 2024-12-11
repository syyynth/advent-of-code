from collections import Counter

with open('input.txt') as f:
    data = f.readlines()


def parse_two_lists():
    ans = 0
    list1 = []
    list2 = []

    for line in data:
        x, y = map(int, line.split())
        list1.append(x)
        list2.append(y)

    list1.sort()
    list2.sort()

    return list1, list2


def part1():
    ans = 0
    l1, l2 = parse_two_lists()

    for x, y in zip(l1, l2):
        ans += abs(x - y)

    return ans


def part2():
    ans = 0
    l1, l2 = parse_two_lists()

    count_l2 = Counter(l2)

    for el in l1:
        ans += el * count_l2[el]

    return ans


print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
