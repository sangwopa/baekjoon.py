# A의 index인 idx와 B의 index인 ch_idx 관리
# 가장 작은 수부터 비교하기 위해 sort
# B가 크지 않다면 다음 B로 넘어가면서 비교
def solution(A, B):
    answer = 0
    idx, ch_idx = 0, 0
    A.sort()
    B.sort()
    
    while idx < len(A) and ch_idx < len(B):
        while ch_idx < len(B):
            if A[idx] < B[ch_idx]:
                answer += 1
                idx += 1
                ch_idx += 1
                break
            else:
                ch_idx += 1

    return answer

print(solution([5,1,3,7], [2,2,6,8]))
print(solution([2,2,2,2], [1,1,1,1]))