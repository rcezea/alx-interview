#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" Utf-8 validation module"""


def validUTF8(data):
    """ returns true if validation passes else false"""
    extra_bits = 0
    for i in data:
        if not isinstance(data[i], int):
            return False
        if extra_bits == 0:
            if i >> 5 == 0b110:
                extra_bits = 1
            elif i >> 4 == 0b1110:
                extra_bits = 2
            elif i >> 3 == 0b11110:
                extra_bits = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            extra_bits -= 1
    return extra_bits == 0
