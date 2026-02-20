A = int(input())
B = int(input())
C = int(input())

count_A = 0
while A >= C:
    A -= C
    count_A += 1
    print(A)
count_B = 0
while B >= C:
    B -= C
    count_B += 1
    print(B)


sum_A = 0
count_sum = 0

while count_sum < count_B:
    sum_A += count_A
    count_sum += 1


print("Ответ", sum_A)#count_A*count_B)
    
