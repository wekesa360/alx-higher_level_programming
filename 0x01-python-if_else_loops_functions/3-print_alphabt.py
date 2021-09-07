#!/usr/bin/python3
for alphabet in range(97,123,1):
  if chr(alphabet) != 'q' and chr(alphabet) != 'e':
    print("{:c}".format(alphabet), end="")
