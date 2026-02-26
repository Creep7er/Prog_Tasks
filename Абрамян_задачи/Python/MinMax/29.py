from math import inf

# N = int(input())
m = [5,4,3,3,5,6,7,8,9,9,3,3,3,3,7,6]
min_val = inf
count = 0
count_max = 0

posled = False
for i in range(len(m)):
    #input_i = int(input())
    input_i = m[i]
    if input_i < min_val:
        posled = True
        count_max = 1
        min_val = input_i
        count = 1
    elif input_i == min_val:
        if posled:
            count += 1
            if count_max < count:
                count_max = count
        else:
            count = 1
            posled = True


    else:
        posled = False
        count = 0
    print("min_val, i_pred", input_i, min_val, count, count_max)


print(min_val, count_max)
