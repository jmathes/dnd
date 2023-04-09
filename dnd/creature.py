from dataclasses import dataclass

from dnd.stats import Stats


@dataclass
class Creature:
    stats: Stats
