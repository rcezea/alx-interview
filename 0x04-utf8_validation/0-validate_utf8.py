#!/usr/bin/python3

""" Utf-8 validation module"""
from typing import List


def validUTF8(data: List) -> bool:
    """ returns true if validation passes else false"""
    extra_bits = 0
    for i in data:
        # print("loop: ", bin(i))
        if extra_bits == 0:
            # print("again")
            if i >> 5 == 0b110:
                # print(1)
                extra_bits = 1
            elif i >> 4 == 0b1110:
                extra_bits = 2
            elif i >> 3 == 0b11110:
                # print(3)
                extra_bits = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            # print(extra_bits)
            extra_bits -= 1
    return extra_bits == 0


# 1000000 - 2nd, 3rd or 4th byte
# 0000000 - 1 single byte
# 0000110 - 2 bytes
# 1110000 - 3 bytes
# 1111000 - 4 bytes


# 1000000
# 229 - 11100101
# 65 -- 010
# 127 - 01111111
# 256
# 11 - 00001010
# 111 - 01101111
# 111 >> 4 - 00000110
