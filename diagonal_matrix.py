import numpy as np


class DiagonalMatrix:
    """A diagonal matrix modeled as a vector of diagonal entries"""
    def __init__(self, matrix):
        self.d = matrix.shape[0]
        if len(matrix.shape)>1:self.data = np.diag(matrix).copy()
        else: self.data = matrix.copy()
        
    def __add__(self,other):
        """Returns a DiagonalMatrix object by adding element wise the data"""
        if isinstance(other, DiagonalMatrix):
            if self.d == other.d:
                return DiagonalMatrix(self.data + other.data)
            else:
                raise ValueError('Dimensions must agree')
        else:
            raise TypeError('Addition operation is not compatible')
        

    def __mul__(self, other):
        """Multiplying 2 diagonal matrices is just element wise multiplication"""
        if isinstance(other, (int, float)):
            return  DiagonalMatrix(self.data * other)
        elif isinstance(other, DiagonalMatrix):
            if self.d == other.d:
                return DiagonalMatrix(np.multiply(self.data, other.data))
            else:
                raise ValueError('Dimensions must agree')
        else:
            raise TypeError('Multiplication operation is not compatible')
        
    def __sub__(self, other):
        """Subtracting 2 diagonal matrices"""
        other = other * -1
        return self + other
    
    def __truediv__(self, other):
        """Dividing diagonal matrix by a scalar is just element wise division"""
        if isinstance(other, (int, float)):
            return DiagonalMatrix(np.diag(self.data / other))
        else:
            raise TypeError('Division operation is not compatible')

        
    def __repr__(self):
        return f'{self.data}'
    
    def __getitem__(self, i):
        if i >= self.d:
            raise IndexError
        else:
            return self.data[i]
        
    def __setitem__(self, i, val):
        if i >= self.d:
            raise IndexError
        else:
            self.data[i] = val
        
    def invert(self):
        return DiagonalMatrix(1/self.data)
    
    def __len__(self):
        return self.d
    
    def det(self):
        """Returns the determinant of the matrix"""
        return np.prod(self.data)
    
    
if __name__ == '__main__':
    a = DiagonalMatrix(np.array([[1.0, 0.0], [0.0, 4.0]]))
    b = DiagonalMatrix(np.array([[5.0, 0], [0, 8.0]]))
    print(f"Addition of {a} + {b} : {a+b}")
    print(f"Subtraction of {a} - {b} : {a-b}")
    print(f"Multiplication of {a} * 5 : {a*5}")
    print(f"Multiplication of {a} * {b} : {a*b}")
    print(f"Division of {a} / 5 : {a/5}")
    print(f"Length of {a} : {len(a)}")
    a[1] = 8
    print(f"Setting a[1] to 8 :{a}")
    print(f"Inversion of {a} : {a.invert().data}")
    print(f"{a[1]}")
        
    
