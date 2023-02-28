# 다 맞고 시간초과 난 코드
# A를 이기는 가장 작은 수를 뽑아서 배치
# 큰 수가 먼저 나와 나중의 경우를 망칠 것을 대비해 sort
def solution(A, B):
    answer = 0
    A.sort()
    for i in A:
        tmp = [n for n in B if (n-i) > 0]
        
        if len(tmp) == 0:
            break
        else:   
            answer += 1
            B.remove(min(tmp))

    return answer

print(solution([5,1,3,7], [2,2,6,8]))
print(solution([2,2,2,2], [1,1,1,1]))