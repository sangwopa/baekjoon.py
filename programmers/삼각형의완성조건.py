def solution(sides):
    answer = 0
    sides.sort()
    
    for i in range(sides[1]-sides[0], sum(sides)):
        tmp = sides.copy()
        tmp.append(i)
        tmp.sort()
        if tmp[0] + tmp[1] > tmp[2]:
            answer += 1
        else:
            continue           
    return answer

sides1 = [1, 2]
print(solution(sides1))
sides2 = [3, 6]
print(solution(sides2))
sides3 = [11, 7]
print(solution(sides3))