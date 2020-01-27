from __future__ import print_function
from __future__ import division
import numpy as np

A = np.zeros((3,3))
B = np.ones((3,3))
print(np.hstack([A, B]))
print(np.vstack([A, B]))
print(np.dstack([A, B]))
print(np.concatenate([A, B], axis=0))
print(np.concatenate([A, B], axis=1))
