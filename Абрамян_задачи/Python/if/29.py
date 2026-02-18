a = int(input())
text = ''
if a > 0:
    text += 'Положительное'
    if a % 2 == 0:
        text += ' четное'
    else:   text += ' нечетное'
elif a < 0:
    text += 'Отрицательное'
    if a % 2 == 0:
        text += ' четное'
    else:   text += ' нечетное'
else: text += 'нулевое'

print(text, "число")

