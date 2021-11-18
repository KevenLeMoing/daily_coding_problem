"""
Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.
For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
Do this in O(N) time and O(1) space.
"""

import itertools


def my_func(my_list: list) -> int:
    for a, b in itertools.combinations(my_list, 2):
        if a != b:
            if my_list.count(a) == 3:
                continue
        else:
            continue


def compute_o_n(my_list: list) -> int:
    for x in my_list:
        if my_list.count(x) == 1:
            return x