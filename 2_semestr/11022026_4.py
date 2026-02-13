year = int(input())

true_year = 2016

if year % 4 == 0:
    step1 = True
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, 'Высокостный')
        else:
            print(year, 'Несокостный')
    else: print(year, 'Несокостный')
else: print(year, 'Несокостный')



