#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Return a sey=t of all elemnts present in only one set"""
    return (set_1 ^ set_2)