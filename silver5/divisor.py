t = int(input())
a = str(input())

div = a.split(' ')
con = 0

for i in range(t):
    div[i] = int(div[i])

div.sort()

if len(div) == 1:
    con = div[0] * div[0]
elif len(div) % 2 == 0:
    con = div[0] * div[len(div) - 1]
else:
    con = div[len(div)//2]

print(con)