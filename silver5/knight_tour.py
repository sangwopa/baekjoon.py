div = []

for i in range(36):
    div.append(str(input()))

# 모든 체스판을 한번 씩 돌았는지 검증하기 위한 val 리스트
val = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 
'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 
'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 
'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 
'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 
'F1', 'F2', 'F3', 'F4', 'F5', 'F6']

# 처음으로 돌아 올 수 있는지 확인하기 위해 처음위치를 맨 뒤에 붙임
div.append(div[0])
val.append(div[0])

# Knight처럼 움지일 수 있는지를 검증하는 함수
def val_knight(div):
    for i in range(36):
        if div[i][0]=='A':
            a = 1
            b = int(div[i][1])
        elif div[i][0]=='B':
            a = 2
            b = int(div[i][1])
        elif div[i][0]=='C':
            a = 3
            b = int(div[i][1])
        elif div[i][0]=='D':
            a = 4
            b = int(div[i][1])
        elif div[i][0]=='E':
            a = 5
            b = int(div[i][1])
        elif div[i][0]=='F':
            a = 6
            b = int(div[i][1])
        else:
            return False
        if div[i+1][0]=='A':
            c = 1
            d = int(div[i+1][1])
        elif div[i+1][0]=='B':
            c = 2
            d = int(div[i+1][1])
        elif div[i+1][0]=='C':
            c = 3
            d = int(div[i+1][1])
        elif div[i+1][0]=='D':
            c = 4
            d = int(div[i+1][1])
        elif div[i+1][0]=='E':
            c = 5
            d = int(div[i+1][1])
        elif div[i+1][0]=='F':
            c = 6
            d = int(div[i+1][1])
        else:
            return False
        if abs(a-c)==1 and abs(b-d)==2:
            flag = 1
        elif abs(a-c)==2 and abs(b-d)==1:
            flag = 1
        else:
            flag = 2
            break
    if flag == 1:
        return True
    else:
        return False

# 함수 검증 후 플래그 세우기
if val_knight(div)==True:
    flag1 = 1
else:
    flag1 = 0

# 모든 체스판을 한번 씩 돌았는지 검증
div.sort()
val.sort()

if div==val:
    flag2 = 1
else:
    flag2 = 0

# 두개 조건 모두 만족 시 Valid 출력
if flag1 == 1 and flag2 == 1:
    print('Valid')
else:
    print('Invalid')
        