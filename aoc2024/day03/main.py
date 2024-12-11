import re

with open('input.txt') as f:
    data = f.read()


def part1():
    parsed = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)

    return sum(
        int(x) * int(y)
        for x, y in parsed
    )


def part2():
    parsed = re.findall(r'(do\(\))|(don\'t\(\))|mul\((\d{1,3}),(\d{1,3})\)', data)

    ans = 0
    do = True

    for pos, neg, x, y in parsed:
        if neg:
            do = False
        if pos:
            do = True
        if do and x and y:
            ans += int(x) * int(y)

    return ans


print('part 1:', part1())
print('part 2:', part2())
