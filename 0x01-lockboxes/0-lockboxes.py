#!/usr/bin/python3
""" 0. Lock boxes """


def canUnlockAll(boxes):
    """Cracking the lock box"""
    if not type(boxes) is list:
        return 'not a list'

    length = len(boxes)
    keys = {0}
    visited = set()

    while True:
        if not keys:
            return False

        index = keys.pop()

        if (index in visited or index >= length or
                not isinstance(boxes[index], list)):
            continue

        visited.add(index)
        keys.update(boxes[index])

        for k in keys.copy():
            if k >= length or not isinstance(boxes[k], list):
                keys.remove(k)
                continue
            keys.update(boxes[k])
            visited.add(k)
            keys.remove(k)
            if len(visited) == length:
                return True

        if len(visited) == length:
            return True
