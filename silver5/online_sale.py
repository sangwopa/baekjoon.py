N, M = map(int, input().split())

# 요구 금액을 cus 리스트에 나열
cus = []
for i in range(M):
    cus.append(int(input()))

# 오름차순 정렬
cus.sort()

# N, M의 크기에 따른 조건을 나눠 결과 도출
sum = 0
if N >= M: # N이 M 보다 크거나 같다면 모든 고객에 대해 고려 가능
    for i in range(M):
        temp = 0
        for n in range(M):
            if cus[n] >= cus[i]:
                temp += cus[i]
        if sum < temp:
            pri = cus[i]
            sum = temp
else: # M이 N 보다 크다면 줄 수 있는 계란의 개수 한계를 두고 고려를 해야함
    for i in range(1, N+1):
        temp = 0
        for n in range(i):
            temp += cus[M-1-n]
            tmp = M-1-n
        if temp > sum:
            pri = tmp
            sum = temp

print(pri, sum)    