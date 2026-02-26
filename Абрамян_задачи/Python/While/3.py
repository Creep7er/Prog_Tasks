N = int(input("Введите N: "))
K = int(input("Введите K: "))

chastnoe = 0
ostatok = N

while ostatok >= K:
    ostatok -= K
    chastnoe += 1

print("Частное:", chastnoe)
print("Остаток:", ostatok)