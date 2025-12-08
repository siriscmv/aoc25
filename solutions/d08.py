from collections import defaultdict


def parser(input):
    return [tuple(map(int, line.split(","))) for line in input.splitlines()]


def compute_dists(junctions):
    n = len(junctions)
    dists = []

    for i in range(n):
        for j in range(i + 1, n):
            (a, b, c) = junctions[i]
            (d, e, f) = junctions[j]

            dist = (a - d) ** 2 + (b - e) ** 2 + (c - f) ** 2
            dists.append(((a, b, c), (d, e, f), dist))

    dists.sort(key=lambda x: x[2], reverse=True)
    return dists


def simulate(input, count):
    circuits = {}
    id = 1
    dists = compute_dists(input)
    unique_ids = set()
    found = False

    for k in range(count):
        if not dists:
            break
        a, b, _ = dists.pop()

        if a in circuits and b not in circuits:
            circuits[b] = circuits[a]
        elif b in circuits and a not in circuits:
            circuits[a] = circuits[b]
        elif a not in circuits and b not in circuits:
            circuits[a] = id
            circuits[b] = id
            unique_ids.add(id)
            id += 1
        elif circuits[a] != circuits[b]:
            # merge
            final_id = min(circuits[a], circuits[b])
            to_change = max(circuits[a], circuits[b])
            unique_ids.remove(to_change)

            for key in circuits:
                if circuits[key] == to_change:
                    circuits[key] = final_id

        if len(circuits) == len(input) and len(unique_ids) == 1 and not found:
            found = (a, b)

    return circuits, found


def solve(circuits):
    counts = defaultdict(int)
    for key in circuits:
        counts[circuits[key]] += 1

    vals = sorted(counts.values())

    return vals[-1] * vals[-2] * vals[-3]


def p1(input):
    return solve(simulate(input, count=1000)[0])


def p2(input):
    a, b = simulate(input, count=2**20)[1]
    return a[0] * b[0]
