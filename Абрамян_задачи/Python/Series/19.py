N = int(input())

i_pred = int(input())

K = 0

for i in range(-1):
    input_i = int(input())
    if input_i < i_pred:
        print("====", input_i)
        K += 1

print(K)