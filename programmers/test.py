def solution(grid):
    global n, m, answer, directions
    answer = []
    n, m = len(grid), len(grid[0])
    
    #4방향 방문 기록 리스트: y*x*4
    visited = [[[False] * 4 for _ in range(n)] for _ in range(m)]
    
    print(visited)
    
    
grid = ["SL","LR"]
print(solution(grid))
    