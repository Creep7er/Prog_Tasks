from math import inf

count = 0

N = int(input("N? "))
mins = inf
maxs = -inf

for j in range(N):
    i = int(input(f"{j+1}:"))

    if i > maxs:
        maxs = i
        num = j


    count += 1


print(N - num -1)