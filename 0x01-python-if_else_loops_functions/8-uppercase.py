#!/usr/bin/python3
def uppercase(str):
    print("{}".format(''.join(
         (chr(ord(c) - 32)) if 96 < ord(c) < 123 else c for c in str)))
