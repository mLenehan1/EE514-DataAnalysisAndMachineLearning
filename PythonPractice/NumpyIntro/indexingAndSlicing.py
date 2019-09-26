from __future__ import print_function
from __future__ import division
import numpy as np

a = np.arange(25).reshape(5,5)
print(a)

a_bottom = a[2:, :]
print(a_bottom)

a_bottom = a[-3:, :]
print(a_bottom)

a_right = a[:, -2:]
print(a_right)

print(a[-3:, -3:])
print(a[1:-1, 1:-1])

print(a)
a[1:-1, 1:-1] = 50
print(a)