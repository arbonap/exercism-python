# -*- coding: utf-8 -*-
import string


def is_pangram(phrase):

    punctuation = string.punctuation
    alphabet = string.lowercase

    phrase = phrase.lower()
    alphadict = {}

    for char in phrase:
        char = char.strip()
        if char in punctuation:
            continue

        if char not in alphadict:
            alphadict[char] = 1
        else:
            continue

    if len(alphadict) >= 26:
        return True
    return False
