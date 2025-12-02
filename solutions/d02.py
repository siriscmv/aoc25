def parser(input):
    ranges = []

    for range in input.split(","):
        if not range.strip():
            continue

        start, end = range.strip().split("-")
        ranges.append((int(start), int(end)))

    return ranges


def is_invalid(num, p):
    num_str = str(num)
    length = len(num_str)
    mid = length // 2

    if p == 1:
        return length % 2 == 0 and num_str[:mid] == num_str[mid:]

    for i in range(1, mid + 1):
        seq = num_str[:i]
        if seq * (length // i) == num_str:
            return True
    return False


def solve(input, p):
    ans = 0

    for start, end in input:
        for num in range(start, end + 1):
            if is_invalid(num, p):
                ans += num

    return ans


def p1(input):
    return solve(input, p=1)


def p2(input):
    return solve(input, p=2)
