from collections import deque

maze = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

x, y = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((x, y))

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny < 0 or nx >= len(maze) or ny >= len(maze[0]):
            continue

        if maze[nx][ny] == 0:
            continue

        if maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1

            queue.append((nx, ny))


print(maze)