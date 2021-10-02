A, B = map(int,input().split())

n = 1
sum = 0
while B > sum:
    sum += n
    n += 1

con = []
for i in range(1, n):
    for n in range(i):
        con.append(i)

res = 0
for i in range(A, B+1):
    res += con[i]

print(res)



