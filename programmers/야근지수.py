from itertools import product

def solution(n, works):
    answer = 9223372036854775807
    tmp = []
    if sum(works) <= n:
        return 0

    for i in product(range(0, n+1), repeat=len(works)):
        if sum(i) == n:
            tmp.append(i)
    
    for i in tmp:
        lst = [x-y for x, y in zip(works, i)]
        if not all(i > 0 for i in lst):
            continue
        else:
            minimum = sum([x**2 for x in lst])
            if answer > minimum:
                answer = minimum

    return answer


print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1,1]))