import numpy as np
from diagonal_matrix import DiagonalMatrix
from utils import create_matrix, create_Identity
from scipy import linalg

class Matrix:
    """Matrix class nxn with each element be a diagonal matrix of dxd"""
    def __init__(self,n,d,matrix):
        self.n = n
        self.d = d
        self.matrix = matrix
        

    def __repr__(self):
        return f'{self.matrix}'
    
    def __getitem__(self, item):
        return self.matrix[item]
    
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
        
    
    def __mul__(self, other):
        """
        1.Multiply 2 Matrices with each other
        2.Multiplying a matrix by a scalar is just element wise multiplication
        """
        if isinstance(other, (Matrix)):
            return Matrix(self.n, self.d, self.matrix@other.matrix)
        
        if isinstance(other, (int, float)):
            return Matrix(self.n, self.d, self.matrix * other)
        
    def inverse(self):
        """Returns the inverse of the matrix using Gauss Jordon from scratch"""
        
            

    

if __name__ == '__main__':
    m = Matrix(2, 2, create_matrix(2, 2))
    print(m)
    print((m*m))
    print(m*2)
    A= m.inverse()
    print(A*m)

    