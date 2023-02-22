from collections import deque

start = [0, 0]
end = [0, 4]
maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]

col_len = len(maps[0])
row_len = len(maps)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_way(maps, start, end):
    distance = deque([0])
    queue = deque([])
    queue.append(start)
    visited = {
        0: [start]
    }
    
    col_len = len(maps[0])
    row_len = len(maps)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]   
    
    while 1:
        stts = 0
        for i in range(len(queue)):
            if queue[i][0] == end[0] and queue[i][1] == end[1]:
                stts += 1
                continue            
            cnt = 0
            for n in range(4):
                nx = queue[i][0] + dx[n]
                ny = queue[i][1] + dy[n]   
                
                if nx == -1 or nx == col_len or ny == -1 or ny == row_len or  maps[nx][ny] == 'X':
                    continue 
                
                if (maps[nx][ny] in ('O', 'L', 'E')) and not [nx, ny] in visited[i]:
                    if cnt >= 1:
                        queue.append([nx, ny])
                        distance.append(distance[i])
                        visited[i+1] = visited[i]
                    else:
                        queue[i] = [nx, ny]
                    cnt += 1
                    distance[i] += 1
                    visited[i].append([nx, ny])
        else:
            if stts == len(queue):
                break
                
    return min(distance)

print(find_way(maps, start, end))
