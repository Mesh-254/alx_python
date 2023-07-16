#!/usr/bin/python3
for n in range(0, 99):
    print("{:02d},".format(n), end=" ")
    if n == 98:
        print("99", end="\n")
