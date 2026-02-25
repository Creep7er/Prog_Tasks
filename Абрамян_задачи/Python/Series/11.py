
n = int(input("Сколько? "))
K = int(input("Сколько? "))
kek = False

for i in range(n):
    input_i = int(input(""))
    if input_i < K:
        kek = True
    
    
print(kek)