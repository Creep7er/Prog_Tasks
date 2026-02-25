from math import inf

n = int(input("Сколько? "))

sum = 0
proizv = 1

for i in range(n):
    input_i = float(input(""))
    input_i = input_i - int(input_i)


    print(input_i)
    proizv *= input_i
    
print("Произведение", proizv)