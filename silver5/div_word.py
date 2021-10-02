wrd = str(input())

# n>=3 일 때, 세개의 수를 합해서 n이 나오는 모든 경우의 수
def three_sum(n):
    con = []
    for i in range(1,n-1):
        for p in range(1, n-i):
            u = n - i - p
            temp = [i, p, u]
            con.append(temp)
    return con

div = three_sum(len(wrd))
con = []

# 각 경우의 수대로 단어를 나눠서 역순정리 후 결과 리스트에 붙이고 오름차순정렬
for i in range(len(div)):
    a = []
    b = []
    c = []
    for n in range(div[i][0]):
        a.append(wrd[n])
    for n in range(div[i][0], div[i][1]+div[i][0]):
        b.append(wrd[n])
    for n in range(div[i][1]+div[i][0], div[i][1]+div[i][0]+div[i][2]):
        c.append(wrd[n])
    a.reverse()
    b.reverse()
    c.reverse()
    temp = a + b + c
    tmp = ''
    for i in range(len(temp)):
        tmp += temp[i]
    con.append(tmp)

con.sort()

print(con[0])