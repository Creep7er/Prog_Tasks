import random
from math import inf
# ------- Заполнение массива
N = int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
print(lst)

# ------- Заполнение массива

step = len(lst) - 1
i = 0
x = 0
y = 0



while step >= 1:
    while i + step < len(lst):
        if lst[i] > lst[step + i]:
            lst[i], lst[step + i] = lst[step + i], lst[i]
        i += 1
    step = int(step / 1.247)
    print("222", lst)
print(lst)
    