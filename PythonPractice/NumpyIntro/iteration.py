from __future__ import print_function
from __future__ import division
import numpy as np

A = np.arange(9).reshape(3, 3)
for row in A:
    print(row)
for i, row in enumerate(A):
    print('row', i, '=', row)

A = np.arange(27).reshape(3, 3, 3)
for matrix in A:
    print(matrix)