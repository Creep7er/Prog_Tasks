from math import inf

n = int(input("Сколько? "))
max_val = -inf
min_val = inf
first_max_index = 0
last_min_index = 0

for j in range(1, n + 1):
    i = int(input(f"{j}:"))

    if i > max_val:
        max_val = i
        first_max_index = j

    if i < min_val:
        min_val = i
        last_min_index = j
    elif i == min_val:
        last_min_index = j

print(f"Номер первого максимального: {first_max_index}")
print(f"Номер последнего минимального: {last_min_index}")