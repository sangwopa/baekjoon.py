A, B, C = map(int, input().split())

D = (((A**2) * (B**2)) / (B**2) + (C**2))**0.5

print(int(D))
print(int(D * (C / B)))