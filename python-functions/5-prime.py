#!/usr/bin/python3
def is_prime(number):
    """function that prints prime numbers"""
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if (number % i) == 0:
                return  False
        return True
    return False
