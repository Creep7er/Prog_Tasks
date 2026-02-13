n = int(input())
f = 0
m = n*2 - 1
S = 0
for i in range(1, n, 2):
    f = (-1)**2 * float(i / i+1)
    print(f)
    S = S + f
    print(S)
print(S)