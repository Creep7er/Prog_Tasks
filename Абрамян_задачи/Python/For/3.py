A = int(input())
B = int(input())
count = 0 
for i in range(B-1, A-1, -1):
    print(i)
    count += 1

print(count)