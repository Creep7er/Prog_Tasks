print("Введите число повторений: ")
tries = int(input())

i = 0
positive = 0
zero = 0
negative = 0
while i <= tries:
    i = i + 1
    a = int(input())
    if a < 0:
        negative = negative + 1

    if a == 0:
        zero = zero + 1
    if a > 0:
        positive = positive + 1
    
print(positive, zero, negative)
