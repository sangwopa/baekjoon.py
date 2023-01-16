import math

def solution(n,a,b):
    answer = 0
    tot = n
    for i in range(21):
        if math.pow(2, i) == n:
            answer = i
            break
    
    while n > 1:
        n = int(n/2)
        if (a <= n and b <= n):
            answer -= 1
            continue
        elif (a > n and b > n):
            a = n*2+1 - a
            b = n*2+1 - b
            answer -= 1
            continue            
        else:
            return answer


n = 8
a = 4
b = 7
print(solution(n,a,b))

n = 16
a = 15
b = 16
print(solution(n,a,b))

