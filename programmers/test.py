import heapq

works =  [4, 3, 3]
n = 4

works = [-w for w in works]
print(works)
heapq.heapify(works)
print(works)

while n > 0:
    max_val = heapq.heappop(works)
    heapq.heappush(works, max_val+1)
    n -= 1
    
print(max_val)

