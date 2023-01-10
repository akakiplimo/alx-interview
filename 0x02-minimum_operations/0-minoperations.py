#!/usr/bin/python3
"""Minimum Operations python3 challenge"""


def minOperations(n):
    """
    calculates the fewest number of
    operations needed to result in exactly n H
    characters in this file.
    Returns:
        Integer : if n is impossible to achieve, return 0
    """
    present_chars = 1  # how many chars in the file
    clipboard = 0  # how many H's copied
    counter = 0  # operations counter

    while present_chars < n:
        # if did not copy anything yet
        if clipboard == 0:
            # copyall
            clipboard = present_chars
            # increment operations counter
            counter += 1

        # if haven't pasted anything yet
        if present_chars == 1:
            # paste
            present_chars += clipboard
            # increment operations counter
            counter += 1
            # continue to next loop
            continue

        remaining = n - present_chars  # remaining chars to Paste
        # check if impossible by checking if clipboard
        # has more than needed to reach the number desired
        # which also means num of chars in file is equal
        # or more than in the clipboard.
        # in both situations it's impossible to achieve n of chars
        if remaining < clipboard:
            return 0

        # if it can't be divided
        if remaining % present_chars != 0:
            # paste current clipboard
            present_chars += clipboard
            # increment operations counter
            counter += 1
        else:
            # copyall
            clipboard = present_chars
            # paste
            present_chars += clipboard
            # increment operations counter
            counter += 2

    # if got the desired result
    if present_chars == n:
        return counter
    else:
        return 0
