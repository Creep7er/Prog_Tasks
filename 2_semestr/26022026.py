import random
N = int(input(''))

A = []

for i in range(N):
    A.append(random.randint(1, 99))

print(A)