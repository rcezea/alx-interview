#!/usr/bin/python3
""" Module to parse strings from standard input """

import sys
import re

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


log_pattern = re.compile(
    r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*?\] '
    r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)

try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if not match:
            continue
        parts = line.split()
        if len(parts) != 9:
            continue

        method = parts[4]
        url = parts[5]
        protocol = parts[6]
        file_size = parts[-1]
        status_code = parts[-2]

        if method != '"GET' or url != '/projects/260':
            sys.exit()

        try:
            status_code = int(match.group(1))
            file_size = int(match.group(2))
        except (IndexError, ValueError, KeyError):
            pass

        total_size += file_size
        if status_code in valid_codes:
            status_counts[status_code] = (
                    status_counts.get(status_code, 0) + 1)

        lines_processed += 1
        if lines_processed % 10 == 0:
            print_stats()

except (KeyboardInterrupt, EOFError):
    print_stats()
    sys.exit()

finally:
    print_stats()
