from collections import deque

# section의 요소들만 검증
# 맨 앞 요소를 끝으고 페인트를 칠한다고 생각
def solution(n, m, section):
    if len(section) == 1:
        return 1
    
    answer = 1
    section = deque(section)
    idx = section.popleft() + m
    
    while section:
        tmp = section.popleft()
        if tmp < idx:
            continue
        else:
            answer += 1
            idx = tmp + m  
                              
    return answer
 
print(solution(8, 4, [2, 3, 6]))
print(solution(5, 4, [1, 3]))
print(solution(4, 1, [1, 2, 3, 4]))