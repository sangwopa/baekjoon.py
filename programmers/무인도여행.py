from collections import deque

# BFS 그래프 순회 방식으로 무인도 거주 일수 return
def rounding_island(visited, maps, start):
    term = int(maps[start[0]][start[1]])
    queue = deque()
    queue.append((start[0], start[1]))
    visited.append((start[0], start[1]))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]        
    
    while queue:
        x, y = queue.popleft()    
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]    
            
            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                continue  
            
            if maps[nx][ny] == 'X':
                continue
            
            if (nx, ny) not in visited:
                term += int(maps[nx][ny])
                queue.append((nx, ny))
                visited.append((nx, ny))

    return term

def solution(maps):
    answer = []
    visited= []

    for i in range(len(maps)):
        for n in range(len(maps[i])):
            if maps[i][n] != 'X' and (i, n) not in visited:
                answer.append(rounding_island(visited, maps, [i, n]))

    answer.sort()
    
    if len(answer) == 0:
        return [-1]
    else:
        return answer


print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
print(solution(["XXX","XXX","XXX"]))


