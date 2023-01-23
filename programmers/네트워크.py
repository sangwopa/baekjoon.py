def solution(n, computers):
    answer = 0
    graph = dict()

    for i in range(len(computers)):
        graph[i] = []
        for n in range(len(computers[i])):
            if n == 1 and n != i:
                graph[i].append(n)    
    
    
    
    
    
    
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))