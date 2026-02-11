x_1 = int(input("x1: "))
x_2 = int(input("x2: "))
y_1 = int(input("y1: "))
y_2 = int(input("y2: "))

width = abs(x_2 - x_1)
height = abs(y_2 - y_1)

P = 2 * (width + height)
S = width * height

print("P:", P)
print("S:", S)