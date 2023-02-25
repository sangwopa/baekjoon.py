from collections import deque

def find_way(maps, start, end):
    distance = 0
    queue = deque([])
    queue.append(start)
    visited = deque([])
    visited.append([start])
    stts = 0
    cnt = 0
    col_len = len(maps[0])
    row_len = len(maps)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]   
    
    while stts != 1:
        cnt += 1
        tmp_queue = deque([])
        tmp_visited = deque([])
        for i in range(len(queue)):    
            for n in range(4):
                nx = queue[i][0] + dx[n]
                ny = queue[i][1] + dy[n]   
                
                if queue[i][0] == end[0] and queue[i][1] == end[1]:
                    stts += 1
                    return distance                 
                
                if nx == -1 or nx == col_len or ny == -1 or ny == row_len or  maps[nx][ny] == 'X':
                    continue 
                
                if (maps[nx][ny] in ('O', 'L', 'E', 'S')) and not [nx, ny] in visited[i]:
                    visited[i].append([nx, ny])
                    tmp_queue.append([nx, ny])
                    tmp_visited.append(visited[i])                
        else:
            distance += 1
            queue = tmp_queue.copy()
            visited = tmp_visited.copy()
        
        if cnt > (col_len*row_len):
            return -1
    
    return -1

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