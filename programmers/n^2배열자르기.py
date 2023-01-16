def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        row = i//n + 1
        if (i+1) % n == 0:
            col = n
        else:
            col = (i+1) % n
        if (row) >= (col):
            answer.append(row)
        else:
            answer.append(col)

    return answer
print(solution(3, 2, 5))
print(solution(4, 7, 14))