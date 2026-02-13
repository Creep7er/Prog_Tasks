n = int(input())
S = 0
for x in range(1, n+1):
    f = 1 
    for y in range(1, x+1):
        f *= y
    S += -f / x**3
    print(f"S += {-f} / {x**3}")

print(S)