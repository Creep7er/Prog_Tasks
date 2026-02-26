from math import inf

n = int(input("Сколько?"))
min_val = inf
first_min_index = 0
last_min_index = 0

for j in range(1, n+1):
    i = int(input(f"{j}:"))

    if i < min_val:
        min_val = i
        first_min_index = j
        last_min_index = j 
    elif i == min_val:
        last_min_index = j

print(f"Номер первого минимального: {first_min_index}")
print(f"Номер последнего минимального: {last_min_index}")