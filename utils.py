import numpy as np
from diagonal_matrix import DiagonalMatrix


def create_matrix(n,d):
    """ Creates a matrix of size nxn where each element is diagonal matrix of dxd"""
    # return np.array([[DiagonalMatrix(np.diag(np.random.randint(1,9,(d)))) for _ in range(n)]for _ in range(n)])
    M = np.empty((n,n), dtype=object)
    for i in range(n):
        for j in range(n):
                M[i,j] = DiagonalMatrix(np.diag(np.random.rand((d))))
    return M

def create_Identity(n, d):
    """ Creates a matrix of size nxn where where every element is diagonal and represents an identity matrix of size n*d x n*d"""
    M = np.empty((n,n), dtype=object)
    for i in range(n):
        for j in range(n):
                if i==j:
                     M[i,j] = DiagonalMatrix(np.diag(np.ones(d, dtype=float)))
                else:
                    M[i,j] = DiagonalMatrix(np.diag(np.zeros(d, dtype=float)))
    return M

def create_specialized(n, d):
    """ Creates a matrix of size nxn where where every element is diagonal and represents an identity matrix of size n*d x n*d"""
    counter = 1
    M = np.empty((n,n), dtype=object)
    for i in range(n):
        for j in range(n):
                M[i,j] = DiagonalMatrix(np.diag(np.ones(d, dtype=float))*counter)
                counter+=1
    return M

if __name__=='__main__':
    M= create_matrix(3, 3)
    print(M)
    print(M.shape)
    print(type(M[0,0]))
