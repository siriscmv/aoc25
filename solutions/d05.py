def parser(input):
    ranges, to_check = input.split("\n\n")
    ranges = [sorted(map(int, line.split("-"))) for line in ranges.splitlines()]
    ranges = [(lo, hi) for lo, hi in ranges]
    to_check = [int(line) for line in to_check.splitlines()]

    ranges.sort()

    return ranges, to_check


def p1(input):
    ranges, to_check = input
    ans = 0

    for num in to_check:
        for lo, hi in ranges:
            if lo <= num <= hi:
                ans += 1
                break

    return ans


def p2(input):
    ranges, _ = input

    ans = 0
    curr_lo, curr_hi = ranges[0]

    for lo, hi in ranges[1:]:
        if lo <= curr_hi + 1:
            curr_hi = max(curr_hi, hi)
        else:
            ans += curr_hi - curr_lo + 1
            curr_lo, curr_hi = lo, hi

    ans += curr_hi - curr_lo + 1
    return ans
