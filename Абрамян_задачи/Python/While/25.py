N = int(input())

a2 = 0
a1 = 1
a0 = a1 + a2
while a0 <= N:
    a0 = a1 + a2
    a2 = a1
    a1 = a0

print(a1)