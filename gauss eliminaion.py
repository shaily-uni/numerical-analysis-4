def gauss_elimination(a):
    n = len(a)
    for i in range(n):
        max_row = i
        for k in range(i+1, n):
            if abs(a[k][i]) > abs(a[max_row][i]):
                max_row = k
        a[i], a[max_row] = a[max_row], a[i]
        for k in range(i+1, n):
            factor = a[k][i] / a[i][i]
            for j in range(i, n+1):
                a[k][j] -= factor * a[i][j]
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = a[i][n] / a[i][i]
        for k in range(i-1, -1, -1):
            a[k][n] -= a[k][i] * x[i]

    return x
aug_matrix = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]
solution = gauss_elimination(aug_matrix)
print("Solution:", solution)
