from math import inf

n = int(input("Сколько? "))
min_val = inf
max_val = -inf
last_extreme_index = 0

for j in range(1, n+1):
    i = int(input(f"{j}:"))

    if i < min_val:
        min_val = i
        last_extreme_index = j
    elif i > max_val:
        max_val = i
        last_extreme_index = j 
    elif i == min_val or i == max_val:
        last_extreme_index = j

print(f"Номер последнего экстремального числа: {last_extreme_index}")