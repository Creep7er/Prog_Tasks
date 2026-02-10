a = [1, 2, 3, 2, 5]
k = 3

if k > len(a) or k <= 0:
    max_sum = 0
else:
    current_sum = sum(a[:k])
    max_sum = current_sum
    for i in range(k, len(a)):
        current_sum = current_sum - a[i - k] + a[i]
        if current_sum > max_sum:
            max_sum = current_sum
            
print(f"Массив: {a}")
print(f"Длина отрезка (k): {k}")
print(f"Максимальная сумма максимального отрезка: {max_sum}")

