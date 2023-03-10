# 틀린 풀이
# 테스트 케이스 5번째가 일치하지 않음
# 자신보다 점수가 높지만 인센티브 못 받으면 뒤로 빼야함
def solution(scores):
    tmp = dict()
    tmp[0] = sum(scores[0])
    
    for i in range(1, len(scores)):
        if scores[0][0] < scores[i][0] and scores[0][1] < scores[i][1]:
            return -1
        else:
            tmp[i] = sum(scores[i])
            
    tmp = {k: v for k, v in sorted(tmp.items(), key=lambda item: (-item[1], item[0]))}
    
    answer = list(tmp.keys()).index(0) + 1

    return answer

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]])) # 4
print(solution([[2, 2], [2, 2], [2, 3], [3, 2]])) # 3
print(solution([[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]])) # 1
print(solution([[3, 1], [1, 4], [2, 3], [2, 3], [1, 5], [1, 0], [1, 0]])) # 5
print(solution([[4,1],[2,4],[3,5]])) # 2
