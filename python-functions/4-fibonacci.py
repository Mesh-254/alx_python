#!/usr/bin/python3
def fibonacci_sequence(n):
    """Return a list of fibonnaci sequences"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[len(fib_sequence) - 1] + \
            fib_sequence[len(fib_sequence) - 2]
        fib_sequence.append(next_num)
    return fib_sequence
