#!/usr/bin/python3
import sys
n = len(sys.argv)
if n == 1:
    print("{} argument:".format(n))
    arg = sys.argv[0]
    print("1: {}".format(arg),end= '')
elif n > 1:
 print("{} arguments:".format(n))
 for i in range(1, n):
    print("{}: {}".format(i, sys.argv[i]))