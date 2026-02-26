N = int(input())

sum = 0
for i in range(N, 2 * N + 1):
    sum += i * i

print(sum)