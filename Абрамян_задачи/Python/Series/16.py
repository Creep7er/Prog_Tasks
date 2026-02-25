from math import inf

K = int(input("K? "))
j = 0
last_index = 0 

while True:
    j += 1
    i = int(input(f"{j}:"))
    if i == 0:
        break

    if i > K:
        last_index = j

print(last_index)