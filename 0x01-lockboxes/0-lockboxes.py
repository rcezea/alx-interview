#!/usr/bin/python3
""" 0. Lock boxes """


def canUnlockAll(boxes):
    """Cracking the lock box"""
    if not type(boxes) is list:
        return 'not a list'
    if not boxes:
        return False
    length = len(boxes)
    keys = {0}
    visited = set()
    while True:
        if not keys:
            return False
        index = keys.pop()
        if index not in visited:
            visited.add(index)
            keys.update(boxes[index])

            for k in keys.copy():
                keys.update(dict.fromkeys(boxes[k]))
                visited.add(k)
                # keys.remove(k)

            if len(visited) == length:
                return True
        else:
            continue
