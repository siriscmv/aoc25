def parser(input):
    return [list(line) for line in input.splitlines()]


def simulate(input, x, y, split, memo):
    r, c = len(input), len(input[0])

    while input[x][y] != "^":
        if x + 1 == r - 1:
            return 1
        x += 1

    if (x, y) in memo:
        return memo[(x, y)]

    if (x, y) not in split:
        split.add((x, y))

    total = 0
    if y > 0:
        total += simulate(input, x, y - 1, split, memo)
    if y < c - 1:
        total += simulate(input, x, y + 1, split, memo)

    memo[(x, y)] = total
    return total


def get_start(grid):
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == "S":
                return r, c
    return None


def solve(input):
    x, y = get_start(input)
    split = set()
    memo = {}

    total = simulate(input, x, y, split, memo)
    return split, total


def p1(input):
    return len(solve(input)[0])


def p2(input):
    return solve(input)[1]
