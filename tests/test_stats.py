from numbers import Number

import pytest

from dnd import dice
from dnd.stats import Stat, Stats


@pytest.fixture
def mock_dice_roll(mocker):
    return mocker.patch.object(dice, "roll")


def describe_Stat():
    def describe_score():
        @pytest.mark.parametrize("score", range(1, 20))
        def it_has_a_score(score: int):
            stat = Stat(score)
            assert stat.score == score

        @pytest.mark.parametrize("before", range(1, 20))
        @pytest.mark.parametrize("after", range(1, 20))
        def it_can_be_set(before: int, after: int):
            if before == after:
                pytest.skip()
            stat = Stat(before)
            assert stat.score == before

            stat.score = after
            assert stat.score == after

        @pytest.mark.parametrize("score", range(1, 20))
        def it_can_be_compared_to_ints_and_floats(score: int):
            stat = Stat(score)

            assert stat.score == score

            assert score == stat
            assert stat == score
            assert stat >= score
            assert score <= stat

            assert stat > score - 1
            assert stat >= score - 1
            assert score + 1 > stat
            assert score + 1 >= stat

            assert stat < score + 1
            assert stat <= score + 1
            assert score - 1 < stat
            assert score - 1 <= stat

        @pytest.mark.parametrize("score", range(1, 20))
        @pytest.mark.parametrize("diff", range(-2, 2))
        def can_add_ints_to_stats(score: int, diff: int):
            stat = Stat(score)
            assert isinstance(stat + diff, Stat)
            assert (stat + diff).score == score + diff
            assert isinstance(diff + stat, Stat)
            assert (diff + stat).score == score + diff

        @pytest.mark.parametrize("score", range(1, 20))
        @pytest.mark.parametrize("diff", range(-2, 2))
        def can_subtract_ints_from_stats(score: int, diff: int):
            stat = Stat(score)
            assert isinstance(stat - diff, Stat)
            assert (stat - diff).score == score - diff
            assert isinstance(diff - stat, Stat)
            assert (diff - stat).score == score - diff

    def describe_modifier():
        def it_calculates_the_modifier():
            stat = Stat(10)
            assert stat.modifier == 0

            stat.score = 12
            assert stat.modifier == 1

            stat.score = 9
            assert stat.modifier == -1

    def describe_roll():
        def it_rolls_n_dice_and_returns_a_Stat(mock_dice_roll):
            mock_dice_roll.side_effect = [4, 2, 5, 6]
            stat = Stat.roll(n=4)
            assert stat.score == 15

        def it_rolls_n_dice_and_returns_a_Stat_independent_of_order(mock_dice_roll):
            mock_dice_roll.side_effect = [2, 5, 6, 4]
            stat = Stat.roll(n=4)
            assert stat.score == 15

        def it_rolls_n_dice_and_returns_a_Stat_unchanged_by_changing_lowest_value(mock_dice_roll):
            mock_dice_roll.side_effect = [4, 1, 5, 6]
            stat = Stat.roll(n=4)
            assert stat.score == 15

        def it_rolls_n_dice_and_returns_a_Stat_other_values(mock_dice_roll):
            mock_dice_roll.side_effect = [4, 5, 5, 6]
            stat = Stat.roll(n=4)
            assert stat.score == 16


def describe_Stats():
    def describe_roll():
        def it_rolls_n_dice_for_each_stat_and_returns_a_Stats_object(mock_dice_roll):
            rolls = []
            rolls += [4, 2, 5, 6]  # str
            rolls += [3, 1, 5, 2]  # dex
            rolls += [6, 6, 1, 3]  # con
            rolls += [5, 6, 2, 4]  # int
            rolls += [1, 6, 5, 2]  # wis
            rolls += [1, 6, 2, 3]  # cha
            mock_dice_roll.side_effect = rolls
            stats = Stats.roll()
            assert stats.strength.score == 15
            assert stats.dexterity.score == 10
            assert stats.constitution.score == 15
            assert stats.intelligence.score == 15
            assert stats.wisdom.score == 13
            assert stats.charisma.score == 11
