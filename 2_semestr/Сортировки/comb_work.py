import random
from math import inf
# ------- Заполнение массива
N = int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
print(lst)
# ------- Заполнение массива
lst_true = lst[:]
for i in range(len(lst_true)):
    for x in range(i, len(lst_true)):
        if lst_true[i] >= lst_true[x]:
            lst_true[i], lst_true[x] = lst_true[x], lst_true[i]

print(lst_true)

# -------- сортирую для проверки
step = len(lst) - 1

while step >= 1:


    for i in range(len(lst) - step):
        if lst[i] > lst[step + i]:
            lst[i], lst[step + i] = lst[step + i], lst[i]
        print("222", lst)
    step = int(step / 1.247)
print(lst)

if lst == lst_true:
    print("отсортирован правильно")
else:
    print('Твой алгоритм плох как js')
    