a = int(input())

val = a
num_ten = 0
num_one = 0
cnt = 0

while(1):
    num_ten = a//10
    num_one = a%10
    a = 10*(num_one) + (num_ten+num_one)%10
    cnt += 1
    if val == a:
        break

print(cnt)