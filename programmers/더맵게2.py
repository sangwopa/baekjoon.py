from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    tmp = -1
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        
        a = heappop(scoville)
        b = heappop(scoville)
            
        tmp = a + (b * 2)
        heappush(scoville, tmp)
        answer += 1
        
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1,2,1,1,1,1,1,1,1], 50))
print(solution([1,1], 3))