from collections import defaultdict

#스택
def iterative_dfs(start_v, graph):
    discovered = []
    stack = [start_v]
    while stack :
        v = stack.pop()
        if v not in discovered :
            discovered.append(v) 
            for w in graph[v] :
                stack.append(w) 
    return discovered

def solution(k, computers):
    answer = 0
    
    graph = defaultdict(list)

    for i in range(len(computers)):
        for n in range(len(computers[i])):
            if i != n and computers[i][n] == 1:
                graph[i].append(n)

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))