#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        keys = a_dictionary.keys()
        sorted_values = sorted(a_dictionary.values())
        score = sorted_values[-1]
        for key in keys:
            if a_dictionary[key] == score:
                return key
