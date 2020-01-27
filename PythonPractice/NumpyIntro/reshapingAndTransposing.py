from __future__ import print_function
from __future__ import division
import numpy as np

A = np.arange(9)
print(A)

A = A.reshape(3,3)
print(A)

print(A.T)
A = np.random.rand(10, 10, 3)
print(A.shape)

print(A.transpose(2, 0, 1).shape)