#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if not tuple_a:
        x, x_ = 0, 0
    elif len(tuple_a) == 1:
        x, x_ = tuple_a[0], 0
    else:
        x, x_ = tuple_a[0], tuple_a[1]
    if not tuple_b:
        y, y_ = 0, 0
    elif len(tuple_b) == 1:
        y, y_ = tuple_b[0], 0
    else:
        y, y_ = tuple_b[0], tuple_b[1]
    result = (x + y, x_ + y_)
    return result
