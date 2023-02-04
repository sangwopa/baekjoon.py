# 동적계획법 이용
# 단계별로 각 자리에 최대값 저장
def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            tmp = land[i-1][j]
            land[i-1][j] = -1
            land[i][j] += max(land[i-1][0], land[i-1][1], land[i-1][2], land[i-1][3])
            land[i-1][j] = tmp
            
    return max(land[len(land)-1])


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))