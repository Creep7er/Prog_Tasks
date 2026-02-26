from math import inf

n = int(input("Сколько чисел будете вводить? "))
min_val = inf
max_val = -inf
first_extreme_index = 0

for j in range(1, n+1):
    i = int(input(f"{j}:"))

    if i < min_val or i > max_val:
        if i < min_val:
            min_val = i
        if i > max_val:
            max_val = i
        if first_extreme_index == 0:
            first_extreme_index = j

print(f"Номер первого экстремального числа: {first_extreme_index}")