import re # 정규표현식 사용

temp = str(input())
con = ''
flag = 0

# X가 하나라도 보이면 붙어있는 X 붙여서 리스트화
div = re.findall('X*', temp)
div.pop(len(div)-1) # 맨 뒤에 '' 가 생겨서 삭제


# '' 항목 모두 . 으로 치환
for i in range(len(div)):
    if div[i]=='':
        div[i] = '.'

# 조건에 따라 폴리오미노로 변경하고 con 문자열에 붙이기 예외일 경우 고려해서 flag 세우기
for i in range(len(div)):
    if div[i][0] == 'X':
        if len(div[i])%4==0:
            con += 'AAAA'*(len(div[i])//4)
        elif len(div[i])%2==0:
            con += 'AAAA'*(len(div[i])//4) + 'BB'
        else:
            flag = 1
            break            
    else:
        con += div[i]

# 조건에 따라 결과 출력 혹은 에러 출력
if flag == 1:
    print(-1)
else:
    print(con)