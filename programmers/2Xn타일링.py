from itertools import combinations, permutations, product
from math import factorial as fc
from functools import reduce

def solution(n):
    answer = 0
    for i in range(n//2 + 1):
        two_num = i
        one_num = n - (2 * i)
        
        answer += (fc(two_num + one_num) / (fc(two_num)*fc(one_num))) % 1000000007
  
    return int(answer) 

print(solution(4))
print(solution(7))