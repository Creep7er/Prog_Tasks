from math import inf

count = 0
j = 0
min_val = inf

while True:
    j += 1
    i = int(input(f"{j}:"))
    if i == 0:
        break

    if i < min_val:
        min_val = i
    if min_val == inf:
        count += 1

print(min_val)