# 최소공배수 구하기
def common_multiple(a, b, c):
    for i in range(max(a,b,c),(a*b*c)+1):
        if i%a==0 and i%b==0 and i%c==0:
            return i
        
from functools import reduce
        
def solution(arr):
    answer = 0
    for i in range(max(arr), reduce(lambda x, y: x * y, arr)+1):
        if not False in [i%n==0 for n in arr]:
            return i    
    return answer

arr = [2,6,8,14]
print(solution(arr))

arr = [1,2,3]
print(solution(arr))