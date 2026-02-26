from math import inf

B = int(input("B? "))
min_val = inf
min_index = 0

for j in range(1, 11):
    i = int(input(f"{j}:"))
    
    if i > B and i < min_val:
        min_val = i
        min_index = j

if min_index == 0:
    print(0)
    print(0)
else:
    print(min_val)
    print(min_index)