import random
from math import inf
# ------- Заполнение массива
N = int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
print(lst)

# ------- Заполнение массива

for i in range(len(lst)):
    for x in range(i, len(lst)):
        if lst[i] >= lst[x]:
            lst[i], lst[x] = lst[x], lst[i]

print(lst)