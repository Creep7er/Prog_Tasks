import random
import time
from math import inf
# ------- Замер времени
start = time.perf_counter()
# ------- Заполнение массива
N = 20000000 #int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
#print(lst)
# ------- Заполнение массива


maxs = -inf
mins = inf
for i in range(len(lst)):
    min_index = i

    for x in range(i, len(lst)):
        if lst[x] < lst[min_index]:
            min_index = x

    lst[i], lst[min_index] = lst[min_index], lst[i]






end = time.perf_counter()
# ------- Замер времени
print('Затрачено', end - start, 'секунд')
#print(lst)