import math
import numpy as np
import numpy.linalg

a = np.zeros((3, 3))
for i in range (3):
    a[i, i] = 4
a[0, 1] = -1
a[1, 0] = -1
a[1, 2] = -1
a[2, 1] = -1

inv_a = np.linalg.inv(a)

v = np.zeros((3, 1))
v[1, 0] = 1
inv_v = v

for i in range(10):
    v = np.matmul(a, v)
    inv_v = np.matmul(inv_a, inv_v)
    if (i == 4):
        max_eigval = np.linalg.norm(v, np.inf)
        min_eigval = 1/ np.linalg.norm(inv_v, np.inf)
    v = v/ np.linalg.norm(v, np.inf)
    inv_v = inv_v/ np.linalg.norm(inv_v, np.inf)
    if (i == 4):
        max_eigvec = v
        min_eigvec = inv_v

print("maximum eigenvalue is: ")
print(max_eigval)
print("\n")
print("maximum eigenvector is: ")
print(max_eigvec)
print("\n")
print("minimum eigenvalue is: ")
print(min_eigval)
print("\n")
print("minimum eigenvector is: ")
print(min_eigvec)

print(np.linalg.eigvals(a))


a = np.array([[3, -3], [5, -8]])
print(np.linalg.eigvals(a))