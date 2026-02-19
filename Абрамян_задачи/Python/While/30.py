A = int(input())
B = int(input())
C = int(input())

count_A = 0
while A >= C:
    A -= C
    count_A += 1
#    print(A)
count_B = 0
while B >= C:
    B -= C
    count_B += 1
#    print(B)

print("Ответ", count_A*count_B)

    
