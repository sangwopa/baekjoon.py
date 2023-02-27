from collections import deque

# 그리디
# 첫 지점이 가장 앞으로 오게 정렬 후
# 다음 지점이 계산중인 모든 지점 범위 안에 들어오면 in 아니면 out
def solution(routes):
    answer = 1
    
    routes.sort(key=lambda x: (x[0]))
    routes = deque(routes)

    queue = deque([])
    queue.append(routes.popleft())

    while len(routes) != 0:
        for i in queue:
            if routes[0][0] > i[1]:
                answer += 1
                queue = deque([])
                queue.append(routes.popleft())                
                break
        else:
            queue.append(routes.popleft())

    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))
print(solution([[-20,-15], [-14,-5]]))
print(solution([[-20,-15]]))
