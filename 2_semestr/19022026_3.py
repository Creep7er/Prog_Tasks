from math import inf

n = int(input("Сколько? "))

sum = 0

maxs = -inf
mins = inf

for i in range(n):
    input_i = int(input(""))
    if input_i > maxs:
        maxs = input_i
    elif input_i < mins:
        mins = input_i
    sum += input_i
    
print("Среднее арифметическое", (sum - mins - maxs) / (n-2))