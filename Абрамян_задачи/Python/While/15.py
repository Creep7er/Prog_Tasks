P = int(input())

S = 1000
K = 0


while S < 1100:
    S += S * P * 0.01
    print(S)
    K += 1
print("Месяцев", K-1)
print("Вклад ", S)

    