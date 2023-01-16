from functools import reduce
from math import factorial

def solution(n):
    answer = 1
    for i in range(1, n//2 + 1): 
        answer += factorial(n-i)//factorial(n-2*i)//factorial(i)
    return answer % 1234567


n = 4
print(solution(n))

n = 3
print(solution(n))

n = 10
print(solution(n))

n = 2000
print(solution(n))