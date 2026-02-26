from math import inf

# N = int(input())
m = [1, 1, 2, 3, 4, 5, 6, 99, 99, 0, 11, 11, 99, 99, 99, 99]
max_val = -inf
count = 0
count_min = 0

posled = False
for i in range(len(m)):
    #input_i = int(input())
    input_i = m[i]
    if input_i > max_val:
        posled = True
        count_min = 1
        max_val = input_i
        count = 1
    elif input_i == max_val:
        if posled:
            count += 1
            if count_min > count:
                count_min = count
        else:
            count = 1
            posled = True


    else:
        posled = False
        count = 0
    print("max_val, i_pred", input_i, max_val, count, count_min)


print(max_val, count_min)
