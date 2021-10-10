import math

N, M, K = map(int, input().split())

def combination(n, r):
    con = math.factorial(n)/(math.factorial(n-r)*math.factorial(r))
    return con

res = (1/combination(N, M)) * (K/M)

print(res)
