from collections import Counter
from itertools import combinations

# 이것도 시간초과 1번보다는 줄임
def solution(weights):
    answer = 0
    val = [1, 3/2, 2, 2/3, 4/3, 1/2, 3/4]
    
    cnt = Counter(weights)
    
    lst = list(cnt.keys())
    
    for i in range(len(lst)):
        for n in range(i, len(lst)):
            if lst[i]/lst[n] in val:
                if i == n:
                    answer += len(list(combinations(range(cnt[lst[i]]),2)))
                else:
                    answer += cnt[lst[i]]*cnt[lst[n]]
    
    return answer

print(solution([100,180,360,100,270])) # 4
print(solution([100, 100, 100, 200, 200, 200])) # 15