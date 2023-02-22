#!/usr/bin/python3
"""
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
"""

import sys


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    """
    if total <= 0:
        return 0

    # table[i] will be storing the minimum
    # number of coins required for i value.
    # So table[V] will have result
    table = [0 for i in range(total + 1)]

    # Base case (If given value V is 0)
    table[0] = 0

    # Initialize all table values as Infinite
    for i in range(1, total + 1):
        table[i] = sys.maxsize

    # Compute minimum coins required
    # for all values from 1 to V
    for i in range(1, total + 1):

        # Go through all coins smaller than i
        for j in range(len(coins)):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and
                   sub_res + 1 < table[i]):
                    table[i] = sub_res + 1

    if table[total] == sys.maxsize:
        return -1

    return table[total]
