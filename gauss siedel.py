def gauss_seidel(a, b, tolerance=1e-10, max_iterations=100):
    n = len(a)
    x = [0.0 for _ in range(n)]  

    for iteration in range(max_iterations):
        x_new = x.copy()

        for i in range(n):
            sum1 = sum(a[i][j] * x_new[j] for j in range(i))    
            sum2 = sum(a[i][j] * x[j] for j in range(i + 1, n))   
            x_new[i] = (b[i] - sum1 - sum2) / a[i][i]
        if all(abs(x_new[i] - x[i]) < tolerance for i in range(n)):
            print(f"Converged in {iteration + 1} iterations.")
            return x_new

        x = x_new
    print("Did not converge within the maximum number of iterations.")
    return x
