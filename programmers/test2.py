from collections import deque

start = [0, 0]
end = [0, 4]
maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]

col_len = len(maps[0])
row_len = len(maps)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_way(maps, start, end):
    distance = 0
    queue = deque([])
    queue.append(start)
    visited = []
    
    while queue:
        now = queue.popleft()
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]      
            
            if nx == -1 or nx == col_len or ny == -1 or ny == row_len:
                continue    
            
            if maps[nx][ny] == 'X':
                continue
            
            if nx == end[0] and nx == end[1]:
                distance += 1
                break
            
            if maps[nx][ny] == 'O' and not [nx, ny] in visited:
                
                queue.append([nx, ny])
                visited.append([nx, ny])
                distance += 1
                
    return distance

print(find_way(maps, start, end))
