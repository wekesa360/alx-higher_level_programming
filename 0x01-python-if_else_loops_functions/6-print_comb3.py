#!/usr/bin/python3
for n in range(0,9):
    for m in range (0,10):
        if n == 8 and m == 9:
            print("{:d}{:d}".format(n,m))
        else:
            print("{:d}{:d}".format(n,m), end=", ")

