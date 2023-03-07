from collections import Counter

# 이전 풀이 combination 길이 구햇다가 간단하게 바꾸니 해결
# weights Counter로 개수 센 다음에 진행해야 시간초과 안남
def solution(weights):
    answer = 0
    val = [1, 2/3, 1/2, 3/4]
    
    cnt = Counter(weights)
    
    lst = list(cnt.keys())
    
    for i in lst:
        for n in val:
            if i * n in lst:
                if n == 1:
                    answer += cnt[i]*(cnt[i]-1)/2
                else:
                    answer += cnt[i]*cnt[i*n]
    
    return int(answer)

print(solution([100,180,360,100,270])) # 4
print(solution([100, 100, 100, 200, 200, 200])) # 15        