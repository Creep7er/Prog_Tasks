from math import inf


N = int(input("N? "))

mins = -inf

for i in range(N):
    m = int(input(f"Материал{i+1} m:"))
    v = int(input(f"Материал{i+1} v:"))
    if m/v > mins:
        mins = m/v
        j = i+1


print(mins, j)