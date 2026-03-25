import random
import time
from math import inf

# ------- Заполнение массива
N = int(input('N '))
arr = []

for _ in range(N):
    arr.append(random.randint(1, 99))
#print(arr)
# ------- Заполнение массива

def remove_duplicates(arr):
    result = []
    
    for i in range(len(arr)):
        found = False
        
        for j in range(len(result)):
            if arr[i] == result[j]:
                found = True
                break
        
        if not found:
            result.append(arr[i])
    
    return result

# ------- Замер времени
start = time.perf_counter()

result = remove_duplicates(arr)

end = time.perf_counter()
# ------- Замер времени
#print(result)
print("Время выполнения:", end - start, "секунд")