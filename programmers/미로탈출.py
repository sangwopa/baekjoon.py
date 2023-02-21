from collections import deque

def find_way(maps, start, end):
    distance = 0
    queue = deque([])
    queue.append(start)
    visited = [start]
    stts = 0
    rotate = 0
    
    col_len = len(maps[0])
    row_len = len(maps)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]    
    
    while queue:
        if rotate == 20:
            break
        now = queue.popleft()
        
        if now[0] == end[0] and now[1] == end[1]:
            stts = 1
            break
        
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]      
            
            if nx == -1 or nx == col_len or ny == -1 or ny == row_len:
                continue    
            
            if maps[nx][ny] == 'X':
                continue

            if (maps[nx][ny] in ('O', 'L', 'E')) and not [nx, ny] in visited:
                queue.append([nx, ny])
                visited.append([nx, ny])
                distance += 1
                break
        else:
            queue.append(start)
            rotate += 1
            
                
    if stts == 0:
        return -1
                
    return distance
                

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

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))