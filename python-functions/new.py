#!/usr/bin/python3
def fibonacci(n):
    p=0
    q=1
    i=2
    List=[p,q]
    while i<n:
        fibo=p+q
        # List.append(fibo)
        p=q
        q=fibo
        List.append(fibo)
        i+=1
        return List
        

print(fibonacci(3))