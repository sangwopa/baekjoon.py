def solution(s):
    answer = []
    cnt = 0
    zero_cnt = 0
    while 1:
        tmp = 0
        for i in s:
            if i == '0':
                zero_cnt += 1
                tmp += 1
        s = '1'*(len(s)-tmp)
        s = bin(len(s))[2:]
        cnt += 1
        if s == '1':
            break
    answer.append(cnt)
    answer.append(zero_cnt)
    return answer

s = "110010101001"
print(solution(s))
s = "01110"
print(solution(s))
s = "1111111"
print(solution(s))