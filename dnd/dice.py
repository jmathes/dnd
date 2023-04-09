import random


def roll(sides=20, rolls=1) -> int:
    return sum([random.randint(1, sides) for _ in range(rolls)])
