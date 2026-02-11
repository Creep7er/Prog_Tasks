from math import sqrt

x_1 = int(input("x1: "))
x_2 = int(input("x2: "))
y_1 = int(input("y1: "))
y_2 = int(input("y2: "))

L = sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
print(L)