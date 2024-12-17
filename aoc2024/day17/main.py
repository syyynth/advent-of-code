import re

with open('input.txt') as f:
    ra, rb, rc, *program = [int(x) for x in re.findall(r'(\d+)', f.read())]


def combo_operand(ra, rb, rc, op):
    return {0: 0, 1: 1, 2: 2, 3: 3, 4: ra, 5: rb, 6: rc}[op]


def solve(ra, rb, rc):
    out = []
    pointer = 0

    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1] if pointer + 1 < len(program) else None

        match opcode:
            case 0:
                ra = int(ra / (2 ** combo_operand(ra, rb, rc, operand)))
                pointer += 2
            case 1:
                rb ^= operand
                pointer += 2
            case 2:
                rb = combo_operand(ra, rb, rc, operand) % 8
                pointer += 2
            case 3:
                pointer = operand if ra != 0 else pointer + 2
            case 4:
                rb ^= rc
                pointer += 2
            case 5:
                out.append(combo_operand(ra, rb, rc, operand) % 8)
                pointer += 2
            case 6:
                rb = int(ra / (2 ** combo_operand(ra, rb, rc, operand)))
                pointer += 2
            case 7:
                rc = int(ra / (2 ** combo_operand(ra, rb, rc, operand)))
                pointer += 2

    return out


def part1():
    return ','.join(map(str, solve(ra, rb, rc)))


def part2():
    """
    the correctness is questionable, but it worked for me
    first, with brute force observe that the length of the 'program' is 8^something + some noise for full match
    educated guess(probably):
     - try to match the suffix at len(program)-1..len(program) with increments by 1
     - multiply this number by 8
     - try to match the suffix at len(program)-2..len(program) with increments by 1
     - repeat for the whole 'program'
     will take A LOT OF TIME for some inputs
    """
    idx = len(program) - 1
    i = 0
    while True:
        q = solve(i, rb, rc)
        if q == program[idx:]:
            if q == program:
                return i
            i *= 8
            idx -= 1
        else:
            i += 1


print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
