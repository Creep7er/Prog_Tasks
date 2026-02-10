from random import randint

#array = [22, 32, 64, 12, 435, 86, 100, 2, 43]
N = 10  
array = []
for i in range(N):
    array.append(randint(1, 99))
print(array) 

def comb(array):
    step = int(len(array)/1.247)
    swap = 1
    while step > 1 or swap > 0:
        swap = 0
        i = 0
        while i + step < len(array):
            if array[i] > array[i+step]:
                array[i], array[i+step] = array[i+step], array[i]
                swap += 1
            i = i + 1
        if step > 1:
            step = int(step / 1.247)
            print(array)

comb(array)
