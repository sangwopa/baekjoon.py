tmp = [[1, 3], [2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

def make_graph(lst):
    con = dict()
    for i in lst:
        con.setdefault(i[0], [])
        con.setdefault(i[1], [])
        if not i[1] in con[i[0]]:
            con[i[0]].append(i[1])
        if not i[0] in con[i[1]]:
            con[i[1]].append(i[0])    
            
    print(con)    
    
    return con
 
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

graph = make_graph(tmp)

print(iterative_dfs(1, graph))