import numbers

def solution(n, s):
    answer = []
    length = n
    if s < n:
        return [-1]
    
    while len(answer) != length:
        tmp = s / n    
        
        if not float(tmp).is_integer():
            tmp = int(tmp) + 1
        else:
            tmp = int(tmp)
        
        answer.append(tmp)
        
        s -= tmp
        n -= 1
    
    answer.sort()
    
    return answer

print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))