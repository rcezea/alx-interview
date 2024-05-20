#!/usr/bin/python3
""" Module to parse strings from standard input """

import sys

status_counts = {}
total_size = 0
valid_codes = {200, 301, 400, 401, 403, 404, 405, 500}
lines_processed = 0


def print_stats():
    """print the statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 9:
            continue

        (method, url, protocol, status_code, file_size) = (
            parts[4],
            parts[5],
            parts[6],
            parts[7],
            parts[8],
        )
        if method != '"GET' or url != "/projects/260" or protocol != 'HTTP/1.1"':
            continue

        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        total_size += file_size
        if status_code in valid_codes:
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

        lines_processed += 1
        if lines_processed % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

finally:
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")
