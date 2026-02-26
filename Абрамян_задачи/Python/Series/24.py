#Неправильно

N = int(input())

flag = False
S = 0
for i in range(N):
    input_i = float(input())

    if flag == True and input_i == 0:
        flag = False
    elif input_i == 0:
        flag = True
        S = 0



    if flag:
        S += input_i
    print("S", S)        
print(S)