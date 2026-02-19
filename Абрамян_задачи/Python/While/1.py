A = int(input())
B = int(input())
count = 0
while A >= B:
    A -= B
    count += 1
    print(A)

print(count)

    