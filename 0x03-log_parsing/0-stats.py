#!/usr/bin/python3
import sys
import signal

# Dictionary to store the count of each status code
status_codes_count = {}
# Variable to store the total file size
total_file_size = 0
# List of valid status codes
valid_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
# Counter for the number of lines processed
line_count = 0


def print_stats():
    """Print the current statistics."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print("{}: {}".format(code, status_codes_count[code]))


def signal_handler(sig, frame):
    """Handle the keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)


# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        # Split the line into components
        parts = line.split()

        # Check if the line format is correct
        if len(parts) != 9:
            continue

        ip, dash, date, method, url, protocol, status_code, file_size = (
            parts[0], parts[1], parts[2], parts[3],
            parts[4], parts[6], parts[7], parts[8])

        if (method != '"GET' or url != '/projects/260'
                or protocol != 'HTTP/1.1"'):
            continue

        try:
            # Convert status code and file size to integers
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        # Update the total file size
        total_file_size += file_size

        # Update the count of the status code
        if status_code in valid_status_codes:
            if status_code not in status_codes_count:
                status_codes_count[status_code] = 0
            status_codes_count[status_code] += 1

        # Increment the line counter
        line_count += 1

        # Every 10 lines, print the statistics
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle keyboard interruption gracefully
    print_stats()
    sys.exit(0)
