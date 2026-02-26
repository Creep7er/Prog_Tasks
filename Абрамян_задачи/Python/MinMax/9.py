from math import inf

n = int(input("Сколько?"))
max_val = -inf
first_max_index = 0
last_max_index = 0

for j in range(1, n+1):
    i = int(input(f"{j}:"))

    if i > max_val:
        max_val = i
        first_max_index = j
        last_max_index = j
    elif i == max_val:
        last_max_index = j

print(f"Номер первого максимального: {first_max_index}")
print(f"Номер последнего максимального: {last_max_index}")