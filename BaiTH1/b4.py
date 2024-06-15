import math
x = float(input("x="))
n = int(input("n="))
P = 0.0
if n%2 == 0:
    P = 2016*x
    T = x
    M = 1
    for i in range(1, n):
        T *= x
        M *= 3
        P += T/M
print("P = %0.3f" %P)
