#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s_dict = sorted(a_dictionary)
    for k in s_dict:
        print(f"{k}: {a_dictionary[k]}")
