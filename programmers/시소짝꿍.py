# 이중 반복문 써서 시간초과
def solution(weights):
    answer = 0
    val = [1, 3/2, 2, 2/3, 4/3, 1/2, 3/4]
    
    for i in range(len(weights)):
        for n in range(i+1, len(weights)):
            if weights[i]/weights[n] in val:
                answer += 1

    return answer

print(solution([100,180,360,100,270])) # 4
print(solution([100, 100, 100, 200, 200, 200])) # 15