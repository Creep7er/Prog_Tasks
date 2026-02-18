A = int(input())
B = int(input())
bol = 0

if A > B:
    bol = A
    A = B
    B = bol
    
print(A, B)
