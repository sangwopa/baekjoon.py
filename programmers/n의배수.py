def solution(n, numlist):
    answer = []
    for i in numlist:
        if (i % n) == 0:
            answer.append(i)
    return answer

n = 3
numlist = [4, 5, 6, 7, 8, 9, 10, 11, 12]	
print(solution(n, numlist))
n = 5
numlist = 	[1, 9, 3, 10, 13, 5]
print(solution(n, numlist))
n = 12
numlist = [2, 100, 120, 600, 12, 12]	
print(solution(n, numlist))