A = int(input())
B = int(input())

if A != B:
    if A < B:
        A = B
    elif A > B:
        B = A
else:
    A, B = 0, 0
    
print(A, B)
