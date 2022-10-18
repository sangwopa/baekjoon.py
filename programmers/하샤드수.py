def solution(x):
    tmp = 0
    for i in str(x):
        tmp += int(i)
    if (x%tmp)==0:
        answer=True
    else:
        answer=False
    return answer

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))