from collections import deque


def find_way(maps, start, end):
    
    maze_map = [[1 if n != 'X' else 0 for n in i] for i in maps]
    col_len = len(maps[0])
    row_len = len(maps)    
    stts = 0
        
    queue = deque([])
    queue.append(start)    
    
    # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
    
        # 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 벗어난 경우, 벽인 경우 무시
            if nx < 0 or ny < 0 or nx >= col_len or ny >= row_len or maze_map[nx][ny] == 0:
                continue
            
            # 해당 위치를 처음 방문하는 경우에만 최단 거리 기록
            if maze_map[nx][ny] == 1:
                maze_map[nx][ny] = maze_map[x][y] + 1
                queue.append((nx, ny))
        else:
            stts = 1
    
    if stts == 1:
        return -1
                
    return maze_map[end[0]][end[1]] - 1

def solution(maps):
    answer = 0
    
    start = []
    lever = []
    exit = []

    for i in range(len(maps)):
        for n in range(len(maps[i])):
            if maps[i][n] == 'X' or maps[i][n] == 'O':
                continue
            elif maps[i][n] == 'S':
                start = [i, n]
            elif maps[i][n] == 'L':
                lever = [i, n]
            elif maps[i][n] == 'E':
                exit = [i, n]
        
        if start != [] and lever != [] and exit != []:
            break    
    
    #출발점에서 레버까지
    tmp = find_way(maps, start, lever)
    
    if tmp == -1:
        return -1
    else:
        answer += tmp
    
    #레버에서 출구까지
    tmp = find_way(maps, lever, exit)
    if tmp == -1:
        return -1
    else:
        answer += tmp    

    return answer

print(solution(["SOOOL","XOXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))