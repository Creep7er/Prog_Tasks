

def process_series(A):
    B = []
    C = []

    if not A:
        return B, C

    count = 1
    for i in range(1, len(A)):
        if A[i] == A[i-1]:
            count += 1
        else:
            B.append(count)
            C.append(A[i-1])
    B.append(count)
    C.append(A[-1])
    return A, B

A = [0, 1231, 12312, 5747, 1231425765]
b, c = process_series(A)
print(b, c)