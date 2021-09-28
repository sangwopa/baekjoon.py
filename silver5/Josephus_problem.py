N, K = map(int, input().split())

div = []
con = []
index = K - 1

for i in range(N):
    div.append(i + 1)

for i in range(N):
    while index >= len(div):
        index = index-len(div)
    a = div[index]
    div.pop(index)
    con.append(a)
    index += K-1

print("<", end = '')
print(*con, sep = ', ', end = '')
print(">")


