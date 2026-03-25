import random
import time
from math import inf

# ------- Заполнение массива
N = int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
#print(lst)
# ------- Заполнение массива

# ------- Замер времени
start = time.perf_counter()

aset = set(lst)
lst = list(aset)

end = time.perf_counter()
# ------- Замер времени

##print(lst)
print("Время выполнения:", end - start, "секунд")