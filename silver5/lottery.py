import math

N, M, K = map(int, input().split())

def combination(n, r):
    con = math.factorial(n)/(math.factorial(n-r)*math.factorial(r))
    return con

if M == K:
    res = 1/combination(N, M)
elif K == 1:
    res = (combination(N, M)-combination(N-M, M))/combination(N, M)
elif M > (N/2):
    if k <= (2*M - N):
        res = 1
else:
    res = (combination(M, K)*(N-M)+1)/combination(N, M)

print(res)
