from collections import deque
from itertools import permutations
import math

def is_prime_number(x):
    if x == 1:
        return False
    
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    length = len(numbers)
    numbers = deque(numbers)
    tmp = []
    for i in range(length):
        perm = list(permutations(numbers, i+1))
        tmp.extend([i for i in perm if i[0] != '0'])
    
    tmp = set(tmp)
    
    for i in tmp:
        if is_prime_number(int(''.join(i))):
            answer += 1        
 
    return answer

# print(solution("17")) # 3
print(solution("011")) # 2