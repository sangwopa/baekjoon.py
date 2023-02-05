import heapq

def solution(n, works):
    # 합보다 크면 0
    if sum(works) <= n:
        return 0

    # 최대 힙 구현
    works = [-i for i in works]
    heapq.heapify(works)
    
    # 제일 큰수를 최대한 줄여주는 방식
    while n > 0:
        max_num = heapq.heappop(works)
        heapq.heappush(works, max_num+1)
        n -= 1
    
    return sum([i**2 for i in works])
    
print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1,1]))