# Michigan_state_problem

The problem is given a nxd x nxd structured matrix where every non overlapping dxd element is a diagonal matrix. 

The purpose of this repo is to solve this problem using matrix data structure.

In this data structure each element is a diagonal matrix and hence we define 
elementary operations of a diagonal matrix and use them such that they are efficient.

Basic Steps:

n = 2

d = 2

mat = np.array([[1,0,1,0],[0,1,0,2],[2,0,3,0],[0,4,0,3]])

mat = convert_to_block_diagonal_matrix(mat, 2)

m = Matrix(n, d, mat)

print((m*m)) # Matrix Multiplication

A= Matrix.inverse(n,d,m) # Matrix Inverse

print("The Computed inverse is",A.matrix)

