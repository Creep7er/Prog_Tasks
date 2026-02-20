from math import inf

count = 0

N = int(input("N? "))

maxs = inf
count_min = 0
num = -inf
for j in range(N):
    i = int(input(f"{j+1}:"))

    if i < maxs:
        maxs = i
        count_maxs = 1
    elif i == maxs:
        count_maxs += 1



print(count_maxs)