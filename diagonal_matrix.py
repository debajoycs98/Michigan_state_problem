import numpy as np


class DiagonalMatrix:
    """A diagonal matrix modeled as a vector of diagonal entries"""
    def __init__(self, matrix):
        self.d = matrix.shape[0]
        self.data = np.diag(matrix)
        
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
        other = other * -1
        print(type(other))
        return self + other
        
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

    def __len__(self):
        return self.d
    
    
if __name__ == '__main__':
    a = DiagonalMatrix(np.array([[1, 0], [0, 4]]))
    b = DiagonalMatrix(np.array([[5, 0], [0, 8]]))
    print(f"Addition of {a} + {b} : {a+b}")
    print(f"Subtraction of {a} - {b} : {a-b}")
    print(f"Multiplication of {a} * 5 : {a*5}")
    print(f"Multiplication of {a} * {b} : {a*b}")
    print(f"Division of {a} / 5 : {a/5}")
    print(f"{a[1]}")
        
    
