import numpy as np
from diagonal_matrix import DiagonalMatrix
from utils import create_matrix, create_Identity, create_specialized 
from scipy import linalg
import copy

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
        I = Matrix(2,2,create_Identity(2, 2))

        if (type(matrix)!=type(I)):
            raise TypeError("The two matrices are not of the same type")
        
        for i in range(n):
            pivot = matrix[i,i]
            if pivot.det() == 0:
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
    m = Matrix(2, 2, create_matrix(2, 2))
    # print("The matrix m is",m)
    I = Matrix(2,2,create_Identity(2, 2))
    # print(m*I)
    # print((m*m))
    # print(m*2)
    A= Matrix.inverse(2,2,m)
    print(m.matrix.shape)
    print(A.matrix.shape)
    print("The identity matrix is",A*m)

    