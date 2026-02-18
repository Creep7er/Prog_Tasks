a = int(input())
b = int(input())
c = int(input())

if c <= a <= b or c <= b <= a:
    print (c)
elif b <= a <= c or b <= c <= a:
    print (b)
else:
    print(a)
    
