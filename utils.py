import numpy as np
from diagonal_matrix import DiagonalMatrix


def create_matrix(n,d):
    """ Creates a matrix of size nxn where each element is diagonal matrix of dxd"""
    return np.array([[DiagonalMatrix(np.diag(np.random.rand((d)))) for _ in range(n)]for _ in range(n)])

def create_Identity(n, d):
    """ Creates a matrix of size nxn where where every element is diagonal and represents an identity matrix of size n*d x n*d"""
    M = np.array([
        [DiagonalMatrix(np.diag(np.ones(d,dtype=float))) if i == j else DiagonalMatrix(np.diag(np.zeros(d,dtype=float))) for j in range(n)]
        for i in range(n)
    ])
    return M

if __name__=='__main__':
    M= create_Identity(3, 3)
    print(M)
    print(M.shape)
