def solution(n):
    answer = 0
    if n <= 2:
        return 1
    for i in range(1, n//2+1):
        tmp = 0
        u = i
        while 1:
            tmp += u
            if tmp > n:
                break
            if tmp == n:
                answer += 1
                break
            u += 1
    return answer + 1
            
        
    
print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(15))
