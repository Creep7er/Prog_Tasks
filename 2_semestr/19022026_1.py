from math import inf

n = int(input("Сколько? "))

the_biggest = -inf

for i in range(n):
    input_i = int(input(""))
    if input_i > the_biggest:
        the_biggest = input_i
    
print("Наибольшее", the_biggest)