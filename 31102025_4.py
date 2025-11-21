from random import randint

# array = [22, 32, 64, 12, 435, 86, 100, 2, 43]
N = 10  
array = []
for i in range(N):
    array.append(randint(1, 99))
print(array) 

def insertion(data):
    for i in range(len(data)):
        j = i - 1 
        key = data[i]
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        print(data)

insertion(array)
