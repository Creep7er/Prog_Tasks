a = int(input())

x_1 = a // 100
x_2 = (a // 10) % 10
x_3 = a % 10


i = x_1 < x_2 and x_2 < x_3

print(i)