N, M, K = map(int, input().split())

def combination(n, r):
    p = 1
    c = 1
    while r > 0:
        c *= n
        p *= r
        n -= 1
        r -= 1
    return c/p

p = combination(N, M)
res = 0

# m개중에서 k개 선택 * 나머지 갯수중에서 k를 제외한 수 / 전체 경우의 수
# 주의 할점은 n-m 이 m-k 보다 작은 경우가 존재하는데 이때는 예외처리 해 주어야 함
while M >= K:
    if (N-M)<(M-K):
        K += 1
        continue
    c = combination(M, K) * combination(N-M, M-K)
    res += c/p
    K += 1

print(res)
    