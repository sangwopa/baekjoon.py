n = 1

con =[]

# while 문을 돌려서 0이 입력되면 break 하고 결과 출력
while n:
    n = int(input())
    if n == 0:
        break
    names = [input() for _ in range(n)]
    val = [0]*n
    for i in range(2*n-1): # 두번 나오지 않은 숫자를 검증하여 해당되는 이름 출력
        a = int(input().split()[0])
        val[a-1] += 1
    for i in range(n):
        if val[i] != 2:
            index = i
            break
    con.append(names[index])
    
for i in range(len(con)):
    print(i+1, con[i])