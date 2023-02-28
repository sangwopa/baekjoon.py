from collections import deque
import copy

# 모든 지점을 돌며 각 지점의 최소거리 업데이트
def find_way(maps, start, end):
    queue = deque()
    queue.append((start[0], start[1]))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]       
    
    while queue:
        x, y = queue.popleft()
        
        # end 지점 업데이트 했으면 break
        if x == end[0] and y == end[1]:
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                continue

            if maps[nx][ny] == 0:
                continue

            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1

                queue.append((nx, ny))
    
    if maps[end[0]][end[1]] == 1:
        return -1
    else:
        return maps[end[0]][end[1]] - 1

def solution(maps):
    answer = 0
    
    new_map = []
    
    start = []
    lever = []
    exit = []

    for i in range(len(maps)):
        tmp = []
        for n in range(len(maps[i])):
            # 새 맵 만들기
            if maps[i][n] == 'X':
                tmp.append(0)
            else:
                tmp.append(1)  
                          
            # 시작점, 레버, 종료지점 찾기
            if maps[i][n] == 'X' or maps[i][n] == 'O':
                continue
            elif maps[i][n] == 'S':
                start = [i, n]
            elif maps[i][n] == 'L':
                lever = [i, n]
            elif maps[i][n] == 'E':
                exit = [i, n]

        new_map.append(tmp)
        
    #출발점에서 레버까지
    tmp = find_way(copy.deepcopy(new_map), start, lever)
    
    if tmp == -1:
        return -1
    else:
        answer += tmp
    
    #레버에서 출구까지
    tmp = find_way(copy.deepcopy(new_map), lever, exit)
    if tmp == -1:
        return -1
    else:
        answer += tmp 
  
    return answer

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))
print(solution(["SOOOO", "XXXXX","LOOOO","XXXXX","EOOOO"]))
