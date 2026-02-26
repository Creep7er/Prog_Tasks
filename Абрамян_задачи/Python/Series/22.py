N = int(input())

i_pred = float(input())

K = 0
flag = 0
for i in range(1, N):
    input_i = float(input())
    if input_i > i_pred and flag != 0:
        flag = i

print(flag)