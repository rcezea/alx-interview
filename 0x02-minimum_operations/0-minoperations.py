#!/usr/bin/python3
"""Python module to 0. Minimum Operations"""


def minOperations(n: int) -> int:
    """Return the minimum operation required to get n characters"""
    if n == 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return i + minOperations(n // i)
    return 0
