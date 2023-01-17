from heapq import heappush, heappop, heapify

scoville = [1, 2, 3, 9, 10, 12]

heapify(scoville)

tmp = heappop(scoville) + (heappop(scoville) * 2)





