from collections import defaultdict

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

def make_graph(lst):
    graph = dict()

    for i in range(len(lst)):
        graph.setdefault(i, [])
        for n in range(len(lst[i])):
            if i != n and lst[i][n] == 1:
                graph[i].append(n)    
    
    return graph
    
def solution(n, computers):
    answer = 0
    discovered = []
    idx = 0
    graph = make_graph(computers)
    while 1:
        tmp_iter = iterative_dfs(idx, graph)
        discovered.extend(tmp_iter)
        answer += 1
        if len(discovered) == n:
            break
        idx = min([i for i in range(n) if not i in discovered])
        
    return answer

# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))