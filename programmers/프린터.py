from collections import deque

def solution(priorities, location):
    answer = 0
    imp_max = max(priorities)
    priorities = deque(priorities)
    while 1:
        if len(priorities) == 0:
            break
        if priorities[0] < imp_max:
            if location == 0:
                priorities.append(priorities.popleft())
                location = len(priorities) - 1
            else:
                priorities.append(priorities.popleft())
                location -= 1
        if priorities[0] == imp_max:
            if location == 0:
                answer += 1
                return answer
            else:
                priorities.popleft()
                imp_max = max(priorities)
                location -= 1
                answer += 1


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))