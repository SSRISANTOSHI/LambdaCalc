import numpy as np

def add_matrices(A, B):
    """
    Add two matrices A and B.
    """
    return np.add(A, B)

def multiply_matrices(A, B):
    """
    Multiply two matrices A and B.
    """
    return np.matmul(A, B)

def transpose_matrix(A):
    """
    Transpose of matrix A.
    """
    return np.transpose(A)

def determinant(A):
    """
    Compute the determinant of matrix A.
    """
    return np.linalg.det(A)

def inverse(A):
    """
    Compute the inverse of matrix A, if it exists.
    """
    if np.linalg.det(A) == 0:
        raise ValueError("Matrix is singular and not invertible.")
    return np.linalg.inv(A)

def rank(A):
    """
    Compute the rank of matrix A.
    """
    return np.linalg.matrix_rank(A)

# Example usage
if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print("Matrix A:\n", A)
    print("Matrix B:\n", B)

    print("\nA + B:\n", add_matrices(A, B))
    print("A * B:\n", multiply_matrices(A, B))
    print("Transpose of A:\n", transpose_matrix(A))
    print("Determinant of A:", determinant(A))
    print("Inverse of A:\n", inverse(A))
    print("Rank of A:", rank(A))
