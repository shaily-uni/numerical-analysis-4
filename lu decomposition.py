def lu_decomposition(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for k in range(i, n):
            sum_ = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_
        for k in range(i, n):
            if i == k:
                L[i][i] = 1.0
            else:
                sum_ = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (A[k][i] - sum_) / U[i][i]
    return L, U
A = [
    [2, -1, -2],
    [-4, 6, 3],
    [-4, -2, 8]
]
L, U = lu_decomposition(A)
print("L matrix:")
for row in L:
    print(row)
print("\nU matrix:")
for row in U:
    print(row)
