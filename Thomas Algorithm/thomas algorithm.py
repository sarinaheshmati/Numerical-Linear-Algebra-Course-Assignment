import numpy as np
import time

start = time.time()
def TA(a,b,c,d):
    n = len(d)
    w= np.zeros(n-1,float)
    g= np.zeros(n, float)
    p = np.zeros(n,float)
    
    w[0] = c[0]/b[0]
    g[0] = d[0]/b[0]

    for i in range(1,n-1):
        w[i] = c[i]/(b[i] - a[i-1]*w[i-1])
    for i in range(1,n):
        g[i] = (d[i] - a[i-1]*g[i-1])/(b[i] - a[i-1]*w[i-1])
    p[n-1] = g[n-1]
    for i in range(n-1,0,-1):
        p[i-1] = g[i-1] - w[i-1]*p[i]
    return p

testA = np.arange(4999, dtype=np.float64)
testC = np.arange(4999, dtype=np.float64)
testB = np.arange(5000)
testD = np.arange(5000)

for i in range(4999):
    testA[i] = -1
    testC[i] = -1
for i in range(5000):
    testB[i] = 4
    if (i%2) == 1:
        testD[i] = 1
    else:
        testD[i] = -1

X = TA(testA, testB, testC, testD)
for i in range (len(X)):
    print("x", i, " = ", X[i], "\n")

end = time.time()
print(end - start)