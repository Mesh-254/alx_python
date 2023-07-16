#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# get the last digit of a positive integer using modulo operator (%).
remainder = number % 10
if remainder > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, remainder), end="\n")
elif remainder == 0:
    print("Last digit of {:d} is {:d} and is 0"
          .format(number, remainder), end="\n")
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, remainder), end="\n")
