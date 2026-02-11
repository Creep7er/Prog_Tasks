def knight(x1, y1, x2, y2):
    return (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2)

def knight3(x1, y1, x2, y2):
    for i in range(8):
        for j in range(8):
            if not knight(x1, y1, i, j):
                continue

            for k in range(8):
                for l in range(8):
                    if not knight(i, j, k, l):
                        continue

                    if knight(k, l, x2, y2):
                        return True
    return False


x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

print(knight3(x1, y1, x2, y2))
