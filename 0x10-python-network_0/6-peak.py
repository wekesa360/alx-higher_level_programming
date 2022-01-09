#!/usr/bin/python3
""" Contains the function find_peak"""
def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers"""
    list = list_of_integers
    n = len(list_of_integers)
    if n ==0:
        return
    midpoint = n // 2
    if (midpoint == n - 1 or list[midpoint] >= list[midpoint + 1] and (list[midpoint] == 0 or list[midpoint + 1] >= list[midpoint - 1])):
        return list[midpoint]
    if midpoint != n - 1 and list[midpoint + 1] > list[midpoint]:
        return find_peak(list[midpoint + 1:])
    return find_peak(list[:midpoint])