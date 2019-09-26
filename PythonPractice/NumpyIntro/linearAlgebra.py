from __future__ import print_function
from __future__ import division
import numpy as np

A = np.random.rand(3, 3)
x = np.random.rand(3)
print('A =', A)
print('x =', x)
b = np.dot(A, x)
print('b = Ax =', b)

print(np.dot(A, A.T))

x_soln = np.linalg.solve(A, b)
print(x_soln)

x_hat, residuals, rank, singular_values = np.linalg.lstsq(A, b)
print(x_hat)

A = np.random.rand(5, 3)
x = np.random.rand(3)
b = np.dot(A, x)
x_hat = np.linalg.lstsq(A, b)[0]
print(x)
print(x_hat)
# x_soln = np.linalg.solve(A, b)

A = np.eye(3)
print(np.linalg.det(A))
print(np.linalg.inv(A))
print(np.linalg.pinv(A))
eigenvalues, eigenvectors = np.linalg.eig(A)
print('eigenvalues', eigenvalues)

U, D, V = np.linalg.svd(A)
print(U.shape, D.shape, V.shape)

A_reconstructed = np.dot(np.dot(U, np.diag(D)), V.T)
print(A_reconstructed)
