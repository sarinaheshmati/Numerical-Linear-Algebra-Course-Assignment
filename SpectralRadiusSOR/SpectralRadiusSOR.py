import numpy as np
def calc_rho (matrix, n) :
    D = np.zeros((n, n))
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    for i in range(n):
        D[i, i] = matrix[i, i]
        if i != n - 1:
            L[i + 1, i] = matrix[i + 1, i]
        if i != 0:
            U[i - 1, i] = matrix[i - 1, i]
    Mjacobi = -1 * np.linalg.inv(D) @ (L + U)
    landas = np.linalg.eigvals(Mjacobi)
    rho = max(abs(landas))

    w_opt = 2 / (1 + np.sqrt(1 - rho ** 2))
    return w_opt - 1
for i in range(1, 1000, 100):
    aa = np.zeros((i, i))
    for j in range(i):
        aa[j, j] = 2
        if j != i - 1:
            aa[j + 1, j] = 1
        if i != 0:
            aa[j - 1, j] = 1
    
    print(calc_rho(aa, i))