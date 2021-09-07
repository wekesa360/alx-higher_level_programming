#!/usr/bin/python3
"""Print the alphabet in lowercase, not followed by new line"""
for alphabet in range (97,123,1):
    print("{:c}".format(alphabet), end="")