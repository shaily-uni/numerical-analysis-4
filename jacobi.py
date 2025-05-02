def jacobi(A, b, x0=None, tol=1e-10, max_iterations=100):
    n = len(A)
    x = x0 if x0 else [0.0] * n
    for iteration in range(max_iterations):
        x_new = x.copy()
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            return x_new
        x = x_new
    return x
A = [
    [10, -1, 2, 0],
    [-1, 11, -1, 3],
    [2, -1, 10, -1],
    [0, 3, -1, 8]
]
b = [6, 25, -11, 15]
solution = jacobi(A, b)
print("Solution:", solution)
