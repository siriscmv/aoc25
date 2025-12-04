def parser(input):
    return [list(line.strip()) for line in input.splitlines()]


def is_accessible(grid, x, y):
    near_count = 0
    combinations = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
    ]
    m, n = len(grid), len(grid[0])

    for dx, dy in combinations:
        xx, yy = x + dx, y + dy
        if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == "@":
            near_count += 1

    return near_count < 4


def clean(input, mutate=False):
    ans = 0

    for i, row in enumerate(input):
        for j, cell in enumerate(row):
            if cell == "@" and is_accessible(input, i, j):
                ans += 1
                if mutate:
                    input[i][j] = "."

    return ans


def p1(input):
    return clean(input)


def p2(input):
    ans = 0

    while cleaned := clean(input, mutate=True):
        ans += cleaned

    return ans
