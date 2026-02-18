A = int(input())
B = int(input())
bol = 0

if A != B:
    A = A+B
    B = A+B
else:
    A, B = 0, 0
    
print(A, B)
