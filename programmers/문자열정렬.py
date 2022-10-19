def solution(s):
    low_str = []
    up_str = []
    for i in s:
        if i.isupper():
            up_str.append(i)
        else:
            low_str.append(i)

    low_str.sort(reverse = True)
    up_str.sort(reverse = True)
    answer = ''.join(low_str) + ''.join(up_str)
    return answer

print(solution('ZCbcdefg'))