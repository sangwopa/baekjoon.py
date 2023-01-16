def solution(brown, yellow):
    answer = []
    tot = (brown+yellow)
    for i in range(3, tot//2 +1):
        if (tot % i == 0):
            tmp = tot // i
            if ((i*2) + (tmp-2)*2) == brown:
                answer = [tmp, i]
                break
    return answer


brown = 10
yellow = 2
print(solution(brown, yellow))

brown = 8
yellow = 1
print(solution(brown, yellow))

brown = 24
yellow = 24
print(solution(brown, yellow))
