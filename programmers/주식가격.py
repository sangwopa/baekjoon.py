from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)

    #왼쪽부터 빼내서 차례대로 검증
    while len(prices) != 0:
        tmp = prices.popleft()
        cnt = 0
        for i in prices:
            if tmp > i:
                cnt += 1
                break
            else:
                cnt += 1
        answer.append(cnt)
        
    return answer


print(solution([1, 2, 3, 2, 3]))