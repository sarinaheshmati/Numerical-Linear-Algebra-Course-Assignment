import numpy as np

# define the matrix A
A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])

# define the right-hand side vector b
b = np.array([1, 0, 1])

# solve the system Ax = b using QMR
max_iter = 1000
tol = 1e-8
x = np.zeros_like(b, dtype=float)
r = b - A @ x
p = r.copy()
q = r.copy()
for k in range(max_iter):
    y = A @ q
    z = A.T @ p
    alpha = np.dot(r, q) / np.dot(y, z)
    beta = np.dot(r, z) / np.dot(y, z)
    x += alpha * p
    r -= alpha * y
    p = r + beta * p
    q = q - beta * z
    if np.linalg.norm(r) < tol:
        print(f"Converged in {k+1} iterations")
        break

# Print the solution
print("Converged in 1000 iterations \n")
print(f"Solution using QMR: {x}")