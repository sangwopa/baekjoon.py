from copy import deepcopy

#그래프 형태로 변환
def make_graph(lst):
    con = dict()
    for i in lst:
        con.setdefault(i[0], [])
        con.setdefault(i[1], [])
        if not i[1] in con[i[0]]:
            con[i[0]].append(i[1])
        if not i[0] in con[i[1]]:
            con[i[1]].append(i[0])    
            
    return con

#dfs 그래프 순환
def iterative_dfs(start_v, graph):
    discovered = []
    stack = [start_v]
    while stack :
        v = stack.pop()
        if v not in discovered :
            discovered.append(v) 
            for w in graph[v] :
                stack.append(w) 
    return len(discovered)

def solution(n, wires):
    answer = 100
    graph = make_graph(wires)
    for i in wires:
        graph_tmp = deepcopy(graph)
        graph_tmp[i[0]].remove(i[1])
        
        graph_tmp[i[1]].remove(i[0])
        
        length_tmp = iterative_dfs(list(graph_tmp.keys())[0], graph_tmp)
        
        if abs(n - 2*length_tmp) < answer:
            answer = abs(n - 2*length_tmp)

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))