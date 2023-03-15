def solution(storey):
    answer = 0
    
    while storey > 0:
        storey, mod = divmod(storey, 10)
        
        if mod > 5 or (mod == 5 and storey % 10 >= 5):
            mod = 10 - mod
            storey += 1
            
        answer += mod
    
    return answer

print(solution(16)) # 6
print(solution(2554)) # 16
print(solution(3)) # 3
print(solution(3194)) # 10
print(solution(9000)) # 2
        