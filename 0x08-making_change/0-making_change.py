#!/usr/bin/python3
"""
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while total - coin >= 0:
            total -= coin
            count += 1
        if total == 0:
            return count
    return -1
