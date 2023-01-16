from collections import deque

def solution(priorities, location):
    answer = 0
    pr_que = deque(priorities)
    while 1:
        if max(pr_que) > pr_que[0]:
            pr_que.append(pr_que.popleft())
            if location == 0:
                location = len(pr_que) - 1
            else:
                location -= 1
            continue
        
        if max(pr_que) == pr_que[0]:
            answer += 1
            if location == 0:
                break            
            pr_que.popleft()
            location -= 1
            
    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))