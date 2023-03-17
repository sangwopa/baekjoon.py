import math

tmp = 1024

length = int(math.log2(tmp))

print(length)

for i in range(2048//tmp):
    print(i)