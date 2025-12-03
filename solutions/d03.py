def parser(input):
    return [[int(x) for x in line.strip()] for line in input.splitlines()]


def find_max(bank, count):
    ans = 0
    ix = -1

    for i in range(count):
        ix += 1
        start = ix
        curr_max = bank[start]

        for j in range(start, len(bank) - (count - i - 1)):
            if bank[j] > curr_max:
                ix = j
                curr_max = bank[j]

        ans += curr_max * (10 ** (count - i - 1))

    return ans


def solve(input, count):
    return sum([find_max(bank, count) for bank in input])


def p1(input):
    return solve(input, count=2)


def p2(input):
    return solve(input, count=12)
