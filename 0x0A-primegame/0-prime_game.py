#!/usr/bin/python3
"""
0. Prime Game
"""


def isWinner(x, nums):
    """
    Determine the winner of a game
    based on the strategic removal of prime numbers
    and their multiples from a set of consecutive integers
    :param x: number of rounds
    :param nums: is an array of n
    :return: name of the player that won the most rounds

    I will apply Sieve of Eratosthenes
    to efficiently find all prime numbers
    from 2 to n(included) from
    https://www.geeksforgeeks.org/sieve-of-eratosthenes/
    """
    if x != len(nums) or nums is None or x == 0 or nums == []:
        return None
    # initialize wins per player
    players = {
        "Maria": 0,
        "Ben": 0,
    }
    for n in nums:
        prime = [True for _ in range(n + 1)]
        p = 2
        while (p * p) <= n:
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1

        moves = [i for i in range(n + 1) if prime[i]]

        # count wins for each player
        if len(moves) % 2 == 0:
            players["Ben"] += 1
        else:
            players["Maria"] += 1

    # check and return the player with more points
    if players["Maria"] > players["Ben"]:
        return "Maria"
    elif players["Ben"] > players["Maria"]:
        return "Ben"
    else:
        return None
