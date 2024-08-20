import numpy as np

def projection (v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v2 = np.linalg.norm(v2)
    return (dot_product/norm_v2**2)*v2

def gram_schmidt (M):
    Qh = np.array(M, dtype=np.float64)
    D = np.zeros((len(M), len(M)), dtype=np.float64)
    R = np.identity(len(M), dtype=np.float64)
    n = len(Qh)
    for j in range(n):
        sigma = 0
        for i in range(j):
            sigma += projection(M[j], Qh[i])
        Qh[j] -= sigma
    for i in range (n):
        D[i][i] = np.linalg.norm(Qh[i])
    for j in range (n):
        for i in range (j):
            R[i][j] = (np.dot(M[j], Qh[i])/(np.linalg.norm(Qh[i]))**2)
    return Qh, R, D

def decomposition (M):
    Qh, Rh, D = gram_schmidt(M)
    Qh = np.transpose(Qh)
    D1 = np.linalg.inv(D)
    Q = np.dot(Qh, D1)
    R = np.dot(D, Rh)
    return Q, R

test1 = np.array([[3, -2, 0], [1, 2, 1], [-2, 2, 1]])
test2 = np.array([[1, 1, 1, 1], [-1, 4, 4, -1], [4, -2, 2, 0]])

Q, R = decomposition(test1)
print("Q = ", Q)
print("R = ", R)

Q, R = decomposition(test2)
print("Q = ", Q)
print("R = ", R)