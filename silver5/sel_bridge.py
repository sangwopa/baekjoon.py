import math as mt

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = mt.factorial(m) // (mt.factorial(n) * mt.factorial(m - n))
    print(bridge)
