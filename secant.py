def f(x):
    return x**3 - x - 2
def secant(x0, x1, tol, max_iter):
    print("Iter\tx0\t\tx1\t\tx2\t\tf(x2)")
    for i in range(max_iter):
        if f(x1) - f(x0) == 0:
            print("Division by zero error.")
            return None
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        fx2 = f(x2)
        print(f"{i+1}\t{x0:.6f}\t{x1:.6f}\t{x2:.6f}\t{fx2:.6f}")

        if abs(fx2) < tol:
            return x2

        x0, x1 = x1, x2

    print("Max iterations reached.")
    return x2
x0 = 1
x1 = 2
tolerance = 1e-6
max_iterations = 100

root = secant(x0, x1, tolerance, max_iterations)
print(f"\nApproximate root: {root}")
