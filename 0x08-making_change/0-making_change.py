#!/usr/bin/python3
"""
0-making_change
"""


def makeChange(coins: list, total: int) -> int:
    """
    Determine the fewest number of coins
    needed to meet a given amount total
    """
    new_coins = sorted(coins, reverse=True)
    if total > 0:
        for i in range(len(coins)):
            curr_total = 0
            noOfCoins = 0
            while new_coins:
                max = new_coins[0]
                min = new_coins[-1]
                if curr_total == total:
                    return noOfCoins
                elif (max + curr_total > total) and (
                    min + curr_total > total
                ):
                    noOfCoins += 1
                    break
                elif max + curr_total > total:
                    new_coins.pop(new_coins.index(max))
                else:
                    noOfCoins += 1
                    curr_total += max
            new_coins = sorted(coins, reverse=True)[i + 1:]
        if not coins or noOfCoins > 0:
            return -1
    return 0
