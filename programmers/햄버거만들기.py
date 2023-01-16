def solution(ingredient):
    hamberger = [1,2,3,1]
    
    answer = 0
    n = 0
    cnt = 0
    div = []
    if len(ingredient) < 4:
        return 0
    while 1:
        if len(ingredient) < 4:
            return answer
        if n == (len(ingredient)):
            break
        if cnt == 4:
            for i in range(-1, -5, -1):
                del ingredient[div[i]]
            n = 0
            div = []
            cnt = 0
            continue         
        if ingredient[n] == hamberger[cnt]:
            if cnt == 3:
                answer += 1
            div.append(n)
            cnt += 1
            n += 1
            continue
        if ingredient[n] != hamberger[cnt]:
            n += 1
            cnt = 0
            div = []
            continue
        
    return answer

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))

# ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
# print(solution(ingredient))
