def solution(i, j, k):
    answer = 0
    for n in range(i, j+1):
        tmp = str(n)
        for p in tmp:
            if p == str(k):
                answer += 1
    return answer

i = 1
j = 13
k = 1
print(solution(i, j, k))

i = 10
j = 50
k = 5
print(solution(i, j, k))

i = 3
j = 10
k = 2
print(solution(i, j, k))