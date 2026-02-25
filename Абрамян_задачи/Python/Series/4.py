from math import inf

n = int(input("Сколько? "))

sum = 0
proizv = 1

for i in range(n):
    input_i = int(input(""))
    sum += input_i
    proizv *= input_i
    
print("Сумма", sum)
print("Произведение", proizv)