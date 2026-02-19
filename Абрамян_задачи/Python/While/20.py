N = int(input())

while N > 0:


    if N % 10 == 2:
        print(True)
        break
    N = N // 10
    print(N)