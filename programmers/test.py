from collections import deque

tmp = deque([])
tmp.append(3)
tmp.extend([1,2,3])

print(tmp)
print(1 in tmp)
print(all([i > 1 for i in tmp]))