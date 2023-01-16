from collections import deque

def solution(msg):
    answer = []
    alpha = deque("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    i = 0
    while 1:
        if len(msg) == 0:
            break
        if (i + 1) == len(msg):
            answer.append(alpha.index(msg)+1)
            break
        if msg[:i+1] in alpha and not msg[:i+2] in alpha:
            answer.append(alpha.index(msg[:i+1])+1)
            alpha.append(msg[:i+2])
            msg = msg[i+1:]
            i = 0
        else:
            i += 1
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    return answer

print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))