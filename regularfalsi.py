def f(x):
    return x**3 - x - 2

def regula_falsi(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("Regula Falsi method fails. f(a) and f(b) must have opposite signs.")
        return None

    print("Iter\ta\t\tb\t\tx\t\tf(x)")
    for i in range(1, max_iter + 1):
        x = b - (f(b) * (b - a)) / (f(b) - f(a))
        fx = f(x)
        print(f"{i}\t{a:.6f}\t{b:.6f}\t{x:.6f}\t{fx:.6f}")
        if abs(fx) < tol:
            return x
        if f(a) * fx < 0:
            b = x
        else:
            a = x
    print("Max iterations reached.")
    return x

a = 1
b = 2
tolerance = 1e-6
max_iterations = 100
root = regula_falsi(a, b, tolerance, max_iterations)
print(f"\nApproximate root: {root}")
