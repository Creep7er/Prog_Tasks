a = int(input())
text = ''
if a > 0:
    text += 'Положительное'
    if len(str(abs(a))) == 3:
        text += ' трехзначное'
    elif len(str(abs(a))) == 2:
        text += ' двухзначное'
    else: text += ' однозначное'
elif a < 0:
    text += 'Отрицательное'
    if len(str(abs(a))) == 3:
        text += ' трехзначное'
    elif len(str(abs(a))) == 2:
        text += ' двухзначное'
    else: text += ' однозначное'
else: print('ты ввел Фолси')

print(text, "число")

