#!/usr/bin/python3
for i in range(9):
    for x in range(i + 1, 10):
        if (i * 10) + x <= 88:
            print("{:d}{:d}".format(i, x), end=", ")
print("{:d}".format(89))
