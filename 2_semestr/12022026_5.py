from math import sqrt

n = int(input())
S = 1
q = 0
for x in range(n):
    q = sqrt(2 + q)
    print(q)

print(S)