import math
def f(x):
    return math.cos(x) - x
def df(x):
    return -math.sin(x) - 1
def newton_raphson(x0, tol, max_iter):
    print("Iter\tx\t\tf(x)")
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            print("Zero derivative. No solution found.")
            return None
        print(f"{i+1}\t{x0:.6f}\t{fx:.6f}")
        x1 = x0 - fx / dfx
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    print("Max iterations reached.")
    return x0
initial_guess = 1.0
tolerance = 1e-6
max_iterations = 50
root = newton_raphson(initial_guess, tolerance, max_iterations)
print(f"\nApproximate root: {root}")
