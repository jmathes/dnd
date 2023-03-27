#!/usr/bin/env python3
import json
import os
from pprint import pprint

alphabet = "abcdefghijklmnopqrstuvwxyz"
with open(os.path.join("data", "words.txt"), "r") as wordfile:
    dictionary = [word.lower() for word in wordfile.read().splitlines()]

with open(os.path.join("data", "spells.json")) as spellfile:
    spells = json.load(spellfile)


def try_replacing_letters(word, dictionary):
    word = word.lower()
    for i in range(len(word)):
        for letter in alphabet:
            new_word = word[:i] + letter + word[i + 1 :]
            if new_word in dictionary and new_word != word:
                yield new_word


def try_renaming_spell(spell, dictionary):
    for i, word in enumerate(spell.split()):
        for new_word in try_replacing_letters(word, dictionary):
            yield spell.lower(), (" ".join(spell.split()[:i] + [new_word] + spell.split()[i + 1 :])).lower()


def try_renaming_spells(spells, dictionary):
    for spell in spells:
        for spell_change in try_renaming_spell(spell, dictionary):
            yield spell_change


if __name__ == "__main__":
    for spell, new_spell in try_renaming_spells(spells, dictionary):
        print(f"{spell} -> {new_spell}")
