import numpy as np

# Matrix
#Create a 2*3 matrix
A = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix A:")
print(A)

#Determinant Matrix
B = np.array([[1, 2], [3, 4]])
det_B = np.linalg.det(B)
print("Matrix B:")
print(B)
print("Determinant of B:", det_B)

#penjumlahan matrix
C = np.array([[1,2,3], [4,5,6]])
D = np.array([[7,8,9], [10,11,12]])

E = C + D
print("Matrix E:")  
print(E)

#perkalian matrix
F = np.dot(C, D.T) # D.T untuk transpose D agar sesuai dengan dimensi C
print("Matrix F:")
print(F)

#invers matrix
G = np.array([[1, 2], [3, 4]])
G_inv = np.linalg.inv(G)
print("Matrix G inverse:")
print(G_inv)

#Transpose matrix
H = np.array([[1, 2, 3], [4, 5, 6]])
H_transpose = H.T
print("Matrix H transpose:")
print(H_transpose)

#Vektor
# Extracting vectors from a matrix
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
v_column = A[:, 1]  # Second column as a vector
print(v_column)  # Output: [2 5 8]

v_row = A[2, :]  # Third row as a vector
print(v_row)  # Output: [7 8 9]

# Building a matrix from vectors
v1 = np.array([1, 0, 3])
v2 = np.array([0, 1, 4])
v3 = np.array([1, 1, 1])

M_as_rows = np.array([v1, v2, v3])
print("Matrix M built from vectors as rows:")
print(M_as_rows)

M_as_columns = np.column_stack((v1, v2, v3))
print("Matrix M built from vectors as columns:")
print(M_as_columns)

#Ketergantungan linear
v1 = np.array([[1, 2, 3],[4, 5, 6]])

v1_T = v1.T
print("Vektor v1:")
print(v1)
print("Vektor v1 transpose:")
print(v1_T)

# Rank matrix
E = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

rank_E = np.linalg.matrix_rank(E)
print(rank_E)  # Output: 2

# Eigenvalues dan Eigenvectors
G = np.array([[2, 0],
              [0, 3]])

eigenvalues = np.linalg.eigvals(G)
print(eigenvalues)  # Output: [2. 3.]

