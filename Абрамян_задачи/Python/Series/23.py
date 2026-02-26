#Что изменил - убрал сброс флага по else и вынес его в основной if

N = int(input())
pred_pred = float(input())
pred = float(input())

flag = 0
for i in range(3, N + 1):
    current = float(input())
    
    if not ((pred_pred < pred and pred > current) or (pred_pred > pred and pred < current)):
        if flag == 0:
            flag = i - 1
    
    pred_pred = pred
    pred = current

print(flag)