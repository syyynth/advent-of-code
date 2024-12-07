with open('input.txt') as f:
    data = [
        list(map(int, line.split()))
        for line in f
    ]


def check_helper(line, direction='inc'):
    first = line[0]
    replaces = 0

    for el in line[1:]:
        if (el - first if direction == 'inc' else first - el) not in (1, 2, 3):
            replaces += 1
        else:
            first = el
    return replaces


def check_lvl(line, rem=False, direction='inc'):
    if not rem:
        return check_helper(line, direction) < 1

    idx = 0
    checked = False

    while idx < len(line) - 1:
        inc = line[idx + 1] - line[idx] in (1, 2, 3)
        dec = line[idx] - line[idx + 1] in (1, 2, 3)

        if not inc if direction == 'inc' else not dec:
            if checked or all(check_helper(line[:i] + line[i + 1:], direction) >= 1 for i in [idx, idx + 1]):
                return False
            checked = True
            idx += 2
        else:
            idx += 1

    return True


def part1():
    return sum(
        check_lvl(nums, direction='inc') or check_lvl(nums, direction='dec')
        for nums in data
    )


def part2():
    return sum(
        check_lvl(nums, True, direction='inc') or check_lvl(nums, True, direction='dec')
        for nums in data
    )


print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
