N = int(input())

i_pred = float(input())

K = 0
flag = True
for i in range(N-1):
    input_i = float(input())
    if input_i < i_pred:
        flag = False

print(flag)