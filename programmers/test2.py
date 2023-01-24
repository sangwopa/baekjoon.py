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

tmp = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def make_graph(lst):
    graph = dict()

    for i in range(len(lst)):
        graph.setdefault(i, [])
        for n in range(len(lst[i])):
            if i != n and lst[i][n] == 1:
                graph[i].append(n)    
    
    return graph

   
print(make_graph(tmp))

print(iterative_dfs(2, make_graph(tmp)))