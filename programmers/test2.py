from collections import deque

answer = []
alpha = deque("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
msg = "KAKAO"

print(msg[:1])

if msg[:1] in alpha and not msg[:2]in alpha:
    answer.append(alpha.index(msg[:1])+1)
    msg = msg[1:]
    
    
print(not msg[:2]in alpha)
print(msg)