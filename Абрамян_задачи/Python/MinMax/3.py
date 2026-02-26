from math import inf


N = int(input("N? "))

j = 0
mins = -inf

for _ in range(N):
    j += 1
    a = int(input(f"Прямоугольник{j} a:"))
    b = int(input(f"Прямоугольник{j} b:"))
    if a*b > mins:
        mins = a*b

print(mins)