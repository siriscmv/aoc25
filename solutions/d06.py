def parser(input):
    problems = []

    for line in input.splitlines():
        if not line.strip():
            continue

        ix = 0
        for seq in line.split(" "):
            if not seq.strip():
                continue

            if len(problems) <= ix:
                problems.append([])

            problems[ix].append(seq)
            ix += 1

    return problems, [list(line) for line in input.splitlines() if line.strip()]


def p1(input):
    ans = 0

    for problem in input[0]:
        op = problem[-1]
        numbers = list(map(int, problem[:-1]))

        if op == "*":
            res = 1
            for num in numbers:
                res *= num
        elif op == "+":
            res = sum(numbers)
        else:
            raise ValueError(f"Unknown operation: {op}")

        ans += res

    return ans


def p2(input):
    transposed = list(zip(*input[1])) + [(" ",)]

    ans = 0
    op = None
    nums = []

    for row in transposed:
        if row[-1] in ("*", "+"):
            op = row[-1]

        if any([r != " " for r in row]):
            nums.append(int("".join([r for r in row if r.isdigit()])))
            continue

        if op == "*":
            res = 1
            for num in nums:
                res *= num
        elif op == "+":
            res = sum(nums)
        else:
            raise ValueError(f"Unknown operation: {op}")

        ans += res
        nums = []

    return ans
