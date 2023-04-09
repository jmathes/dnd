import random
from pprint import pprint

import numpy


def roll_die():
    return random.randint(1, 6)


def roll_n_dice(n):
    return [roll_die() for _ in range(n)]


def choose_highest(n, k):
    return sorted(roll_n_dice(n), reverse=True)[: min(n, k)]


allocations = [
    (2, 3, 4, 4, 8, 10),
    (3, 3, 4, 5, 5, 5),
    (1, 4, 4, 8, 8, 8),
    (4, 4, 4, 4, 4, 4),
]

stats = {allocation: [] for allocation in allocations}

for allocation in allocations:
    for i in range(1000):
        charstats = sum([sum(choose_highest(n, 3)) for n in allocation])
        stats[allocation].append(charstats)

for allocation, stat in stats.items():
    print(f"stats with {allocation} dice:")
    print(
        f"mean: {numpy.mean(stat)}, stdev: {numpy.std(stat)}, 25%: {numpy.percentile(stat, 25)}, 50%: {numpy.percentile(stat, 50)}, 75%: {numpy.percentile(stat, 75)}"
    )
    print()


# def pstat(n):
#     return n
#     return int(100 * n) / 100


# stats = [[] for i in range(len(allocations[0]))]

# for i in range(1000):
#     for allocation in allocations:
#         for j, k in enumerate(allocation):
#             stats[j].append(sum(choose_highest(k, 3)))

# for i, stat in enumerate(stats):
#     print(f"stats with {allocations[0][i]} dice:")
#     print(
#         f"mean: {pstat(numpy.mean(stat))}, stdev: {pstat(numpy.std(stat))}, 25%: {pstat(numpy.percentile(stat, 25))}, 50%: {pstat(numpy.percentile(stat, 50))}, 75%: {pstat(numpy.percentile(stat, 75))}"
#     )
#     print()
