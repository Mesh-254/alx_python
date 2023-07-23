#!/usr/bin/python3
for n in range(0, 100):
    if list(str(n)) in list(str(n)):
        continue
    else:
        print(n, end=" ")