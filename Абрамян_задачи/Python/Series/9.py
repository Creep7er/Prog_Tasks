
n = int(input("Сколько? "))

count = 0

for i in range(n):
    input_i = int(input(""))
    if input_i % 2 != 0:
        count += 1
        print(input_i)

    
print("Count", count)