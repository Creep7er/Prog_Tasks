N = int(input())

i_pred = int(input())

K = 0

for i in range(N-1):
    input_i = int(input())
    if i_pred < input_i:
        print("====", i_pred)
        K += 1

print(K)