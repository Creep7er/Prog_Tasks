from math import inf

n = int(input("Сколько? "))

sum = 0
proizv = 1

for i in range(n):
    input_i = float(input(""))
    print(int(input_i))
    sum += int(input_i)
    
print("Сумма", sum)