from math import inf

count = 0

K = int(input("K? "))
j = 0
maxs = -inf
while True:
    j += 1
    i = int(input(f"{j}:"))
    if i == 0:
        break

    if i > K:
        maxs = i
    if maxs == -inf:
        count += 1


print(count+1)