div = list(map(int,input().split())) # 리스트에 나눠 받아오기

div.sort() # 오름차순 정렬

# 최소공배수 구하기
def common_multiple(a, b, c):
    for i in range(max(a,b,c),(a*b*c)+1):
        if i%a==0 and i%b==0 and i%c==0:
            return i

# 세개의 숫자를 뽑아서 리스트에 저장
def pick_three(div):
    con = []
    temp = []
    for i in range(len(div)):
        for u in range(len(div)-1):
            for n in range(len(div)-2):
                if (i+u+n+2 >=len(div)):
                    continue
                temp = [div[i],div[i+u+1],div[i+u+n+2]]
                con.append(temp)            
    return con

con = pick_three(div)

res = 1

for i in range(len(div)):
    res*=div[i]

for i in range(len(con)):
    temp = common_multiple(con[i][0],con[i][1],con[i][2])
    if temp < res:
        res = temp

print(res)   

