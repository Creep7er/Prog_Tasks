a = int(input())
b = int(input())
c = int(input())

ab = a+b
bc = c+b
ac = c+a

if ab <= bc and bc <= ac:
    print (ab + bc)
elif bc <= ab and ac <= ab:
    print (bc + ac)
else:
    print(ac + ab)


