def solution(n):
    ans = 0
    while n > 0:
        if n % 2 == 1:
            n -= 1
            ans += 1
        else:
            n = int(n/2)
    return ans




n = 5
print(solution(n))

n = 6
print(solution(n))

n = 5000
print(solution(n))