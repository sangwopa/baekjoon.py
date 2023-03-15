from itertools import product

def solution(storey):
    answer = []
    
    case = list(product(range(2), repeat=len(str(storey))))
    
    for i in case:
        now = storey
        tmp = 0
        for n in range(len(i)-1, -1, -1):
            if i[n] == 0:
                tmp += int(str(now)[n])
                now -= int(str(now)[n])*(10**(len(i)-(n+1)))
            else:
                tmp += 10 - int(str(now)[n])
                now += (10 - int(str(now)[n]))*(10**(len(i)-(n+1)))     
            
        answer.append(tmp)

    return min(answer) 

print(solution(16)) # 6
print(solution(2554)) # 16
print(solution(3)) # 3
print(solution(3194)) # 10
print(solution(9000)) # 2
    
    