import numpy as np
from diagonal_matrix import DiagonalMatrix
from utils import create_matrix, create_Identity, create_specialized, convert_to_block_diagonal_matrix
from scipy import linalg
import copy
import time
import argparse

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
        
    def transpose(self):
        """Returns the transpose of the matrix"""
        matrix = copy.deepcopy(self.matrix)

        return Matrix(self.n, self.d, matrix.T)
        
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
                
                for m in range(i+1, n):
                    if matrix[m,i].det() != 0:
                        for j in range(n):
                            matrix[i,j], matrix[m,j] = matrix[m,j], matrix[i,j]
                            I[i,j], I[m,j] = I[m,j], I[i,j]
                        pivot = matrix[i,i]
                        break
                if pivot.det()==0:raise ZeroDivisionError('Pivot is 0')
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
        print("The Identity matrix is", matrix)
        print("The transpose matrix is", matrix.transpose())

        # breakpoint()
        return I* matrix.transpose()

            

    

if __name__ == '__main__':
    

    argparser = argparse.ArgumentParser()
    argparser.add_argument('-n', type=int, default=2, help='Dimension of the matrix')
    argparser.add_argument('-d', type=int, default=2, help='Dimension of the diagonal matrix')
    argparser = argparser.parse_args()

    
    m1 = create_matrix(argparser.n, argparser.d)

    print("The matrix m1 is", m1)

    m1 = Matrix(argparser.n, argparser.d, m1)

    m2 = create_matrix(argparser.n, argparser.d)

    print("The matrix m2 is", m2)

    m2 = Matrix(argparser.n, argparser.d, m2)

    print("The result of matrix multiplication m1 * m2",(m1*m2)) # Matrix Multiplication

    A= Matrix.inverse(argparser.n,argparser.d,m1) # Matrix Inverse

    print("The Computed inverse of m1 is",A.matrix)

    print("Identity matrix should be", A*m1)

    #Check if the row exchanges are allowed
    mat = np.array([[0, 1], [1, 1]])

    print("The inverse of the matrix", mat, "is", linalg.inv(mat))

    mat = Matrix(2,1,convert_to_block_diagonal_matrix(mat, 2))

    rat = Matrix.inverse(2, 1, mat) 

    print("The inverse of the matrix", mat, "is", rat)

    