from dataclasses import dataclass
from numbers import Number
from typing import Union

from dnd import dice


@dataclass
class Stat:
    score: int

    def __get__(self):
        return self.score

    def __set__(self, value: int) -> "Stat":
        self.score = value
        return self

    @property
    def modifier(self):
        return (self.score - 10) // 2

    @classmethod
    def roll(cls, n: int = 4) -> "Stat":
        return cls(sum(sorted([dice.roll(6) for _ in range(n)], reverse=True)[:3]))

    def __eq__(self, other: Union["Stat", int, float]) -> bool:
        if isinstance(other, int):
            return self.score == other
        elif isinstance(other, float):
            return abs(self.score - other) < 0.0001
        return self.score == other.score

    def __lt__(self, other: Union["Stat", int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.score < other
        return self.score < other.score

    def __le__(self, other: Union["Stat", int, float]) -> bool:
        return self.score < other or self.score == other

    def __gt__(self, other: Union["Stat", int, float]) -> bool:
        return not self.score < other and not self.score == other

    def __ge__(self, other: Union["Stat", int, float]) -> bool:
        return not self.score < other

    def __add__(self, other: Union["Stat", int]) -> "Stat":
        if isinstance(other, int):
            return Stat(self.score + other)
        return Stat(self.score + other.score)

    def __radd__(self, other: Union["Stat", int]) -> "Stat":
        return self + other

    def __sub__(self, other: Union["Stat", int]) -> "Stat":
        if isinstance(other, int):
            return self + -other
        return Stat(self.score - other.score)

    def __rsub__(self, other: Union["Stat", int]) -> "Stat":
        return self - other


@dataclass
class Stats:
    strength: Stat
    dexterity: Stat
    constitution: Stat
    intelligence: Stat
    wisdom: Stat
    charisma: Stat

    @classmethod
    def roll(cls, n: int = 4) -> "Stats":
        return cls(
            strength=Stat.roll(n),
            dexterity=Stat.roll(n),
            constitution=Stat.roll(n),
            intelligence=Stat.roll(n),
            wisdom=Stat.roll(n),
            charisma=Stat.roll(n),
        )
