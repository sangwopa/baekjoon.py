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
        now = queue.popleft()
        
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]       