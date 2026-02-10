from random import randint

N = 10  
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a) 

for i in range(N-1):
    for j in range(N-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a) 