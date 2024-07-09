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


def convert_to_block_diagonal_matrix(matrix, n):
    """Converts an n*d x n*d numpy matrix into an n x n numpy matrix of DiagonalMatrix objects."""
    n_d, _ = matrix.shape
    if n_d % n != 0:
        raise ValueError("The input matrix size is not compatible with the provided block size.")
    
    d = n_d // n
    new_matrix = np.empty((n, n), dtype=object)
    
    for i in range(n):
        for j in range(n):
            block = matrix[i*d:(i+1)*d, j*d:(j+1)*d]
            if not np.all(block == np.diag(np.diag(block))):
                raise ValueError("The block is not a diagonal matrix.")
            new_matrix[i, j] = DiagonalMatrix(np.diag(np.diag(block)))
    
    return new_matrix

if __name__=='__main__':
    
    mat = [[0,1],[1,1]]
    mat = np.array(mat)
    print(mat.shape)
    mat = convert_to_block_diagonal_matrix(mat, 2)
    print(mat)
    print(create_Identity(2, 1))
