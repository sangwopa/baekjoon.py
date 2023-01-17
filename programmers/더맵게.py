from collections import deque

def solution(scoville, K):
    answer = 0
    scoville.sort()
    tmp_que = deque(scoville)
    
    while 1:
        if len(tmp_que) == 1:
            return -1
        tmp = tmp_que.popleft() + (tmp_que.popleft() * 2)
        tmp_que.append(tmp)
        tmp_que = deque(sorted(tmp_que))
        answer += 1
        if tmp_que[0] < K:
            continue
        else:
            break

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1,2,1,1,1,1,1,1,1], 50))