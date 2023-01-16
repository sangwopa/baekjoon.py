def solution(n):
    bin_n = format(n, 'b')
    cnt = 0
    for i in bin_n:
        if i == '1':
            cnt += 1
    while 1:
        n += 1
        cnt_tmp = 0
        bin_tmp = format(n, 'b')
        for i in bin_tmp:
            if i == '1':
                cnt_tmp += 1
        if cnt == cnt_tmp:
            answer = n
            break  

    return answer

n = 78
print(solution(n))

n = 15
print(solution(n))