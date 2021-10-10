#!/bin/python3
"""
My implementation of the anagram making chalenge.
See details:
https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
"""
import math
import os
import random
import re
import sys
from collections import Counter


def makeAnagram(a, b):
    # Write your code here
    unique_a = set(a)
    unique_b = set(b)

    intersection = unique_a.intersection(unique_b)
    if not intersection:
        # If not intersection, then empty string is the sortest
        # anagram.
        return len(a) + len(b)
    union = unique_a.union(unique_b)

    a_counter = Counter(a)
    b_counter = Counter(b)

    changes = 0
    for elem in union:
        if elem in intersection:
            changes += abs(a_counter[elem] - b_counter[elem])
        elif elem in a_counter:
            changes += a_counter[elem]
        else:
            changes += b_counter[elem]

    return changes


if __name__ == '__main__':
    string1 = input("string1: ")

    string2 = input("string2: ")

    res = makeAnagram(string1, string2)
    print(f"Number of deletion to create an anagram:\nstring1: {string1}\n"
          f"string2: {string2}\nchanges: {res}")
