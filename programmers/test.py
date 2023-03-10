from collections import deque

tmp = [[2,2],[1,4],[3,2],[3,2],[2,1]]

print(tmp)

tmp = {i:sum(tmp[i]) for i in range(len(tmp))}

print(tmp)

tmp = {k: v for k, v in sorted(tmp.items(), key=lambda item: -item[1])}

print(tmp)

lst = list(reversed(tmp.keys()))
    
for i in range(len(lst)):
    for n in range(i+1, len(lst)):
        print(i, n)