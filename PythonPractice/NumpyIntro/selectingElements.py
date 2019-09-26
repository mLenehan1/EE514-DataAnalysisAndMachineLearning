from __future__ import print_function
from __future__ import division
import numpy as np

a = np.arange(9).reshape(3,3)
print(a)

mask = np.eye(3).astype(np.bool8)
print(mask)

print(a[mask])

print(a[[0, 2], :])

print(a[[0, 2], 1])