#!/usr/bin/python3
def uniq_add(my_list=[]):
    """"addition of all unique integers in a list"""
    new_list = set(my_list)
    sum = 0
    for i in set(new_list):
        sum = sum + i
    return sum

