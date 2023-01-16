def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)

def solution(n):
    answer = fibonacci(n) % 1234567
    return answer

n = 3
print(solution(n))

n = 5
print(solution(n))