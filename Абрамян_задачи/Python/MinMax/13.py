
n = int(input("Сколько? "))
index = 0

for j in range(1, n+1):
    i = int(input(f"{j}:"))

    if i % 2 != 0 and index == 0:
        index = j

print(f"{pos_index}")