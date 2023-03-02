from collections import deque

def solution(numbers):
    answer = []
    queue = deque(numbers)
    
    while queue:
        num = queue.popleft()
        
        for i in range(len(queue)):
            if queue[i] > num:
                answer.append(queue[i])
                break
        else:
            answer.append(-1)
  
    return answer

print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))