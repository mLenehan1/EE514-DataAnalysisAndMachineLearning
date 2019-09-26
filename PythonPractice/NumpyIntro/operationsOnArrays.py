from __future__ import print_function
from __future__ import division
import numpy as np

a = np.arange(9).reshape(3,3)
b = np.ones((3,3)) * 2
print(a, b, sep='\n\n')

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a**4)