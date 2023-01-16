from collections import deque

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(len(alpha))

alpha = deque(alpha)

print(alpha)

alpha.append("KA")

print(alpha)


