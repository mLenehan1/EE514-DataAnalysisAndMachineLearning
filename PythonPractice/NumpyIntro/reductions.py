from __future__ import print_function
from __future__ import division
import numpy as np

a = np.arange(9).reshape(3,3)
print(a)
print(np.sum(a))
print(np.sum(a, axis=1))
print(np.sum(a, axis=0))
print(np.sum(a**2))
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))
print(np.std(a))
print(np.var(a))
print(np.median(a))
print(np.max(a))
print(np.min(a))

def zero_one_normalize(a):
    return (a - np.min(a)) / (np.max(a) - np.min(a))

print(zero_one_normalize(a))