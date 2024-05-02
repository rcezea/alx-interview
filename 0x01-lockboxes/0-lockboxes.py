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
        if len(boxes[index]) == 0:
            continue
        if index not in visited and index <= length:
            visited.add(index)
            keys.update(boxes[index])

            for k in keys.copy():
                if len(boxes[k]) == 0 or k > length:
                    continue
                keys.update(dict.fromkeys(boxes[k]))
                visited.add(k)
                keys.remove(k)
                if len(visited) == length:
                    return True

            if len(visited) == length:
                return True
        else:
            continue
