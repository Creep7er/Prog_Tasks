A = [
    [1, 2, 3],
    [4,5,6]

]

def matrix_transponse(A):
    M = len(A)      # Количество строк
    N = len(A[0])   # Количество столбцов

    A_t = []
    for j in range(N):
        A_t.append([])

    for i in range(M):       
        for j in range(N):   
            A_t[j].append(A[i][j])
    print(A_t)

matrix_transponse(A)

