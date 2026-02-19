X = int(input())
N = int(input())
S = 0
for i in range(1, N+1):
    f = 1
    for j in range (1, i+1):
        f *= j
    print(f"{S} = {S} + {X**i}/{f}")
    S = S + (X**i)/f

print(S)