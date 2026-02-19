#Фибоначчи
N = int(input())

a2 = 0
a1 = 1

for i in range(2, N+1):
    a0 = a1 +a2
    a2 = a1
    a1 = a0
    print(a0)

