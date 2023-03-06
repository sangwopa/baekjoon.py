from collections import deque

# 중복을 고려하지 않은 dp로 풀면 시간 초과
def solution(x, y, n):
    answer = 0
    dp = deque([x])
    
    if x == y:
        return 0
    
    while 1:
        answer += 1
        # 똑같은 숫자가 나올수 있는거 방지
        tmp = set()
        while dp:
            num = dp.popleft()
            tmp.add(num*2)
            tmp.add(num*3)
            tmp.add(num+n)
        
        # 해당 요소 있으면 현재 시점 answer return
        if y in tmp:
            return answer
        
        # 모든 요소가 y보다 크면 변환 불가
        if all(i > y for i in tmp):
            return -1
        
        dp.extend(tmp)

    return answer

print(solution(10, 40, 5))
print(solution(10, 40, 30))
print(solution(2, 5, 4))