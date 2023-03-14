# 실패작
def solution(storey):
    answer = 0
    num = str(storey)
    
    if len(num) == 1:
        if storey > 5:
            return (10 - storey) + 1
        else:
            return storey
    
    if int(num[1]) >= 5:
        now = (int(num[0])+1)*(10**(len(num)-1))
        answer += int(num[0])+1
    else:
        int(num[0])*(10**(len(num)-1))
        answer += int(num[0])    
        
    for i in range(1, len(num)):
        if now > storey:
            now -= (10 - int(num[i]))*(10**(len(num)-(i+1)))
            answer += 10 - int(num[i])
        else:
            now += (int(num[i]))*(10**(len(num)-(i+1)))
            answer += int(num[i])
            
    return answer

# print(solution(16)) # 6
print(solution(2554)) # 16
# print(solution(3)) # 3