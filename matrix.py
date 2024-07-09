import numpy as np
from diagonal_matrix import DiagonalMatrix
from utils import create_matrix, create_Identity, create_specialized, convert_to_block_diagonal_matrix
from scipy import linalg
import copy
import time

class Matrix:
    """Matrix class nxn with each element be a diagonal matrix of dxd"""
    def __init__(self,n,d,matrix):
        self.n = n
        self.d = d
        self.matrix = matrix
        

    def __repr__(self):
        return f'{self.matrix}'
    
    
    def __add__(self, other):
        """Add 2 matrices"""
        if isinstance(other, Matrix):
            if self.n == other.n and self.d == other.d:
                return Matrix(self.n, self.d, self.matrix + other.matrix)
            else:
                raise ValueError('Dimensions must agree')
        else:
            raise TypeError('Addition operation is not compatible')
        
    def __sub__(self, other):
        """Subtract 2 matrices"""
        if isinstance(other, Matrix):
            if self.n == other.n and self.d == other.d:
                return Matrix(self.n, self.d, self.matrix - other.matrix)
            else:
                raise ValueError('Dimensions must agree')
        else:
            raise TypeError('Subtraction operation is not compatible')
        
    def __getitem__(self, item1):
        return self.matrix[item1]
    
    def __setitem__(self, key, value):
        self.matrix[key] = value
        
    
    def __mul__(self, other):
        """
        1.Multiply 2 Matrices with each other
        2.Multiplying a matrix by a scalar is just element wise multiplication
        """
        if isinstance(other, (Matrix)):
            return Matrix(self.n, self.d, self.matrix@other.matrix)
        
        if isinstance(other, (int, float)):
            return Matrix(self.n, self.d, self.matrix * other)
        
    @staticmethod    
    def inverse(n,d,m):
        """Returns the inverse of the matrix using Gauss Jordon from scratch"""
        matrix = copy.deepcopy(m)
        I = Matrix(n,d,create_Identity(n, d))

        if (type(matrix)!=type(I)):
            raise TypeError("The two matrices are not of the same type")
        
        for i in range(n):
            pivot = matrix[i,i]
            if pivot.det() == 0:
                #TODO:Allow row exchanges to see if that is possible to make the matrix invertible
                raise ZeroDivisionError('Pivot is 0')
            else:
                for j in range(n):
                    matrix[i,j] = matrix[i,j] * pivot.invert()
                    I[i,j] = I[i,j] * pivot.invert()
                for j in range(n):
                    if i == j:
                        continue
                    temp = matrix[j,i]
                    for k in range(n):
                        matrix[j,k] = matrix[j,k] - matrix[i,k]*temp
                        I[j,k]= I[j,k] - I[i,k]*temp
        
        return I

            

    

if __name__ == '__main__':
    n = 2
    d = 2
    mat = np.array([[1,0,1,0],[0,1,0,2],[2,0,3,0],[0,4,0,3]])
    print("The matrix inverse is", linalg.inv(mat))
    print(mat.shape)
    mat = convert_to_block_diagonal_matrix(mat, 2)
    m = Matrix(n, d, mat)
    # print("The matrix m is",m)
    I = Matrix(n,d,create_Identity(n, d))
    print(m*I)
    print((m*m))
    print(m*2)
    start = time.time()
    A= Matrix.inverse(n,d,m)
    end = time.time()
    print("The time taken to compute the inverse by efficient matrix is", end-start)
    print(m.matrix.shape)
    print("The Computed inverse is",A.matrix)
    print("The identity matrix is",A*m)

    