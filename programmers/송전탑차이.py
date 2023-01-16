cnt = 1
def dfs(graph, visited, start):
    global cnt
    for next_node in graph[start]:
        if not visited[next_node]:
            visited[next_node] = True
            cnt += 1
            dfs(graph, visited, next_node)

def solution(n, wires):
    global cnt
    answer = float('inf')
    
    
    for w in wires:
        tmp = wires[:]
        tmp.remove(w)
        graph = [[] for _ in range(n + 1)]
        
        for a, b in tmp:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * (n + 1)
        networks = []
        for node in range(1, n + 1):
            if not visited[node]:
                visited[node] = True
                cnt = 1
                dfs(graph, visited, node)
                networks.append(cnt)
        
        answer = min(answer, abs(networks[0] - networks[1]))
        
    return answer


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))