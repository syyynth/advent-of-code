with open('input.txt') as f:
    data = []
    for line in f:
        s, *nums = line.split()
        data.append([int(s[:-1]), *map(int, nums)])


def check(nums, oper, s, idx=0, curr=0):
    if idx >= len(nums):
        return [curr]

    if curr > s:
        return []

    results = []
    for op in oper:
        next_val = None
        if op == '+':
            next_val = curr + nums[idx]
        elif op == '*':
            next_val = curr * nums[idx]
        elif op == 'c':
            next_val = int(f'{curr}{nums[idx]}')

        if next_val is not None:
            results += check(nums, oper, s, idx + 1, next_val)

    return results


def part1():
    ans = 0
    for nums in data:
        s, *nums = nums
        poss = check(nums, '+*', s)
        if s in poss:
            ans += s

    return ans


def part2():
    ans = 0
    for nums in data:
        s, *nums = nums
        poss = check(nums, '+*c', s)
        if s in poss:
            ans += s

    return ans


print(f'part1: {part1()}')
print(f'part2: {part2()}')
