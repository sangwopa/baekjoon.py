from collections import deque

answer = 0

lst = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
lst.sort(key=lambda x: (x[0]))

lst = deque(lst)

print(lst)

queue = deque([])

queue.append(lst.popleft())

print(queue)

while len(lst) != 0:
    if lst[0][0] <= queue[0][1]:
        queue.append(lst.popleft())
    else:
        queue.appendleft(lst.popleft())
        answer += 1
        
print(answer)
        
        