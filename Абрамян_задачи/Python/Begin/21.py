from math import sqrt

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
x3 = int(input("x3: "))
y3 = int(input("y3: "))

A = sqrt((x2 - x1)**2 + (y2 - y1)**2)
B = sqrt((x3 - x2)**2 + (y3 - y2)**2)
C = sqrt((x3 - x1)**2 + (y3 - y1)**2)

p = (A + B + C) / 2
S = sqrt(p * (p - A) * (p - B) * (p - C))
print(S)