a = int(input())
b = int(input())
c = int(input())


i = (a > 0 and b > 0) or (c > 0 and a > 0) or (b > 0 and c > 0)

print(i)