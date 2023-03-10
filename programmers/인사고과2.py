# 맞는 풀이지만 시간초과
def solution(scores):
    tmp = {i:sum(scores[i]) for i in range(len(scores))}
    
    tmp = {k: v for k, v in sorted(tmp.items(), key=lambda item: -item[1])}
    
    lst = list(reversed(tmp.keys()))
    
    for i in range(len(lst)):
        for n in range(i+1, len(lst)):
            if scores[lst[i]][0] < scores[lst[n]][0] and scores[lst[i]][1] < scores[lst[n]][1]:
                tmp[lst[i]] = -1
                break
    
    tmp = {k: v for k, v in sorted(tmp.items(), key=lambda item: -item[1])}
    
    if tmp[0] == -1:
        return -1
    else:
        return list(tmp.keys()).index(0) + 1    

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]])) # 4
print(solution([[2, 2], [2, 2], [2, 3], [3, 2]])) # 3
print(solution([[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]])) # 1
print(solution([[3, 1], [1, 4], [2, 3], [2, 3], [1, 5], [1, 0], [1, 0]])) # 5
print(solution([[4,1],[2,4],[3,5]])) # 2
        