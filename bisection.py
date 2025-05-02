def f(x):
    # Example function: Change this to your function
    return x**3 - x - 2

def bisection(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return None

    print("Iter\ta\t\tb\t\tc\t\tf(c)")
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)

        print(f"{i+1}\t{a:.6f}\t{b:.6f}\t{c:.6f}\t{fc:.6f}")

        if abs(fc) < tol or (b - a)/2 < tol:
            return c  # Found root within tolerance

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    print("Max iterations reached.")
    return (a + b) / 2

# Example usage
a = 1
b = 2
tolerance = 1e-6
max_iterations = 100

root = bisection(a, b, tolerance, max_iterations)
print(f"\nApproximate root: {root}")
