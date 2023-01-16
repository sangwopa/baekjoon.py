def solution(ingredient):
    hamberger = [1,2,3,1]
    answer = 0
    
    while 1:
        cnt = 0
        if len(ingredient) < 4:
            break
        for i in range(len(ingredient) - 3):
            if ingredient[i:i+4] == hamberger:
                cnt = 1
                answer += 1
                del ingredient[i+3]
                del ingredient[i+2]
                del ingredient[i+1]
                del ingredient[i]
                break
        if cnt == 0:
            break
    return answer
                


ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))

ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
print(solution(ingredient))