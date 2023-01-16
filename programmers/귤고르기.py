from collections import Counter

def solution(k, tangerine):
    answer = 0
    sum_res = 0
    tmp = Counter(tangerine)
    con2 = {k: v for k, v in sorted(tmp.items(), key=lambda item: item[1], reverse=True)}
    
    for i in con2.values():
        if sum_res >= k:
            break
        else:
            sum_res += i
            answer += 1
    
    return answer
    
    
 

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))