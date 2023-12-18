#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), file=stderr)
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err))
        return False
    else:
        return True
