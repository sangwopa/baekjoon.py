from heapq import *

def solution(numbers):
    n = len(numbers)
    answer = [-1] * n

    h = []

    for i in range(n):
        value = numbers[i]

        while h and h[0][0] < value:
            _, idx = heappop(h)
            answer[idx] = value

        heappush(h, [value, i])

    return answer

print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))   