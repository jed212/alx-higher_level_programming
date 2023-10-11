#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        my_lst = list(a_dictionary.keys())
        score = 0
        first = ""
        for i in my_lst:
            if a_dictionary[i] > score:
                score = a_dictionary[i]
                first = i
        return first
