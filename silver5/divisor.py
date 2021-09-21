t = int(input())
div = list(map(int,input().split()))

con = 0

div.sort()

if len(div) % 2 == 0:
    con = div[0] * div[len(div) - 1]
else:
    con = div[len(div)//2] * div[len(div)//2]

print(con)