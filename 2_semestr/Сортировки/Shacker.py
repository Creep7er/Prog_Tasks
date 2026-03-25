import random
from math import inf
# ------- Заполнение массива
N = int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
print(lst)

# ------- Заполнение массива

left = 0 
right = len(lst) - 1

while left <= right:
    for i in range(right, left, -1):
        if lst[i-1] > lst[i]:
            kekich = lst[i]
            lst[i] = lst[i-1]
            lst[i-1] = kekich
    left += 1
    print(lst)
    for i in range(left, right, +1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
    right -= 1
    print(lst)

print(lst)
    


