def parser(input):
    actions = []

    for line in input.splitlines():
        line = line.strip()
        if not line:
            continue

        dir, count = line[0], line[1:]
        if int(count) == 0:
            raise ValueError("Count cannot be zero")
        actions.append((dir, int(count)))

    return actions


def p1(input):
    curr = 50
    ans = 0

    for dir, count in input:
        if dir == "L":
            curr -= count
        else:
            curr += count

        if curr < 0:
            curr += 100 * (abs(curr) // 100 + 1)

        if curr >= 100:
            curr = curr % 100

        if curr == 0:
            ans += 1

    return ans


def p2(input):
    curr = 50
    ans = 0

    for dir, count in input:
        for _ in range(count):
            if dir == "L":
                curr -= 1
            else:
                curr += 1

            if curr < 0:
                curr += 100

            elif curr >= 100:
                curr = curr % 100

            if curr == 0:
                ans += 1

    return ans
