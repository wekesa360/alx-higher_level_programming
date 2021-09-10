#!/usr/bin/python3
if __name__ == "__main__":
 import sys
 n = len(sys.argv)-1
 if n == 0:
    print("0 arguments.")
 if n == 1:
    print("1 argument:")
    arg = sys.argv[1]
    print("1: {}".format(arg))
 elif n > 1:
    print("{} arguments:".format(n))
    for i in range(1, n):
       print("{}: {}".format(i, sys.argv[i]))