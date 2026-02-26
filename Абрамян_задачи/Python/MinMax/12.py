from math import inf

n = int(input("Сколько? "))
min_val = 0
pos_index = 0

for j in range(1, n+1):
    i = int(input(f"{j}:"))

    if i > 0: 
        if i < min_val:
            min_val = i
            last_extreme_index = j

print(f"{min_val}")