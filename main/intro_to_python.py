import numpy as np

m = np.identity(3, int )

print(m)

m[m == 0] = 3

print(m)

m = np.delete(m, 2, 1)

print(m)

