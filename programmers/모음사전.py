from collections import deque

# 단어 만들기
def make_word(num):
    tmp = {
        0: '',
        1: 'A',
        2: 'E',
        3: 'I',
        4: 'O',
        5: 'U'
    }
    
    lst = deque(str(num))
    
    con = [tmp[int(i)] for i in lst]
    
    return ''.join(con)

# 진법 변환
def base_conv(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]

# 10진법으로 변환
def base_to_ten(n, q):
    con = 0
    for i in range(len(n)):
        con += q**(len(n)-(i+1))*int(n[i])
        
    return con

# 6진법 숫자나열이라 생각하고 길이가 5이하일 때는 오른쪽에 A를 붙여주는 방식으로 구현
def solution(word):
    if word == 'A':
        return 1
    answer = 1
    num = '1'
    while 1:
        answer += 1
        if len(num) < 5:
            num += '1'
        else:
            num = base_to_ten(str(num), 6)
            num = base_conv(num+1, 6)

        if make_word(num) == word:
            break
        
        zero_cnt = str(num).count('0')
        
        if zero_cnt == 2:
            num = str(int(num)//100)
        elif zero_cnt == 3:
            num = str(int(num)//1000)
        elif zero_cnt == 4:
            num = str(int(num[::-1]))

    return answer

# print(solution("A"))
# print(solution("AAA"))
print(solution("AAAAE"))
print(solution("AAAE"))
# print(solution("AAEU"))
# print(solution("AAE"))
# print(solution("AEU"))
# print(solution("E"))
# print(solution("EA"))
print(solution("I"))
print(solution("EIO"))