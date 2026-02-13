n = int(input())
S = 0
for i in range(1, 2*n, 2):
    S += (-1)**(i+1) + i / (i+1)
print(S)