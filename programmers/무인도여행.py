def solution(maps):
    answer = []
    discovered = []
    while len(discovered) < len(maps)*len(maps[0]):
        for i in range(len(maps)):
            for n in range(len(maps[i])):
                if ([i, n] in discovered):
                    continue
                elif maps[i][n] == 'X':
                    discovered.append([i, n])
                    continue
                else:
                    stack = [[i, n]]
                    tmp = 0
                    while stack:
                        v = stack.pop()
                        if v not in discovered :
                            discovered.append(v) 
                            tmp += maps[i, n]
                            
                            
                            
                            
                            for w in graph[v] :
                                stack.append(w)     
                    
                    answer.append(tmp)
                                
                    

                    
    
    
    
    return answer


