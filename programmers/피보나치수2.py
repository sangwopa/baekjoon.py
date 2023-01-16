def fibonacci(n):
    if n == 0 or n == 1:
        return n
    tmp_lst = [0, 1]
    for i in range(n-1):
        tmp_lst.append(tmp_lst[len(tmp_lst)-2] + tmp_lst[len(tmp_lst)-1])
    return tmp_lst[len(tmp_lst)-1]

def solution(n):
    answer = fibonacci(n) % 1234567
    return answer

n = 3
print(solution(n))

n = 5
print(solution(n))