from collections import deque

# 우선순위 큐 사용 풀이
# for 문을 한번만 돌도록 구현
# 끝까지 만족하지 않는 숫자를 위해 -1 배열로 초기화
# 미리 queue에 넣어놓고 조건이 맞으면 빼서 연산
def solution(numbers):
    length = len(numbers)
    answer = [-1]*length
    
    queue = deque([])
    
    for i in range(length):
        value = numbers[i]
        
        while queue and queue[0][0] < value:
            _, idx = queue.popleft()
            answer[idx] = value
            
        queue.appendleft([value, i])
 
    return answer

print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))       
        