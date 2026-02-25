from math import inf

n = int(input("Сколько? "))

sum = 0


for i in range(n):
    input_i = int(input(""))
    sum += input_i
    
print("Среднее арифметическое", sum / n)