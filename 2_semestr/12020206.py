year = int(input())

true_year = 2016

if year % 400 == 0:
    print('В')
elif year % 100 == 0:
    print('Ne')
elif year % 4 == 0:
    print('Visok')
else:
    print('No')



