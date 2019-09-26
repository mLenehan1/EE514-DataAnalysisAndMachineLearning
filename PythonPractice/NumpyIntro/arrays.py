from __future__ import print_function
from __future__ import division
import numpy as np

z = np.zeros(shape=(3,3))
print(z)
print(z.dtype)

z = np.zeros(shape=(3,3), dtype=np.uint8)
print(z.dtype)

x = np.ones((2, 3))
print(x)

x = np.ones((2, 3)) * 5
print(x)

x = np.array([[0,1,0],[1,2,1],[0,1,0]])
print(x)

x = np.eye(4)
print(x)

x = np.ones(10)
print(x)

print(x.shape)
print(x.ndim)

x = np.array([[0,1,0],[1,2,1],[0,1,0]])
print(x[0,0])
print(x[1,0])
print(x[1,1])

np.save('myarray.npy', x)
x_loaded = np.load('myarray.npy')
print(x_loaded)

np.savetxt('myarray.txt', x)
print(np.loadtxt('myarray.txt'))
 