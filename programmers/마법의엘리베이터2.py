# 틀림 헛점이 있음
def solution(storey):
    answer = 0
    
    for i in range(len(str(storey))-1, -1, -1):
        if int(str(storey)[i]) > 5:
            answer += (10-int(str(storey)[i]))
            storey += (10-int(str(storey)[i]))*(10**(len(str(storey))-(i+1)))
        else:
            answer += int(str(storey)[i])
            storey -= int(str(storey)[i])*(10**(len(str(storey))-(i+1)))     
    
    return answer

print(solution(16)) # 6
print(solution(2554)) # 16
print(solution(3)) # 3
print(solution(3194)) # 10