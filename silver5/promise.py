N = int(input())

S = []
A = []

for i in range(N):
    a, b = map(int, input().split())
    S.append(a)
    A.append(b)

max = 0
for i in range(N):
    if abs(S[i]-A[i]) > max:
        max = abs(S[i]-A[i])

time = 0
min = 10**9
res = [] 
for i in range(-max, max+1):
    for n in range(N):
        time += abs(S[n]-A[n]+i)
    if time < min:
        min = time
    res.append(time)

cnt = 0

for i in range(len(res)):
    if res[i] == min:
        cnt+=1

print(cnt)

