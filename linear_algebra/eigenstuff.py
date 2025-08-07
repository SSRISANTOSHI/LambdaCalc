import numpy as np

def eigenvalues_and_vectors(matrix):
    """
    Compute eigenvalues and eigenvectors of a square matrix.

    Parameters:
        matrix (ndarray): A square NumPy array.

    Returns:
        eigenvalues (ndarray): The eigenvalues of the matrix.
        eigenvectors (ndarray): The corresponding eigenvectors.
    """
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square to compute eigenvalues.")
    
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

# Example usage
if __name__ == "__main__":
    A = np.array([[2, 1],
                  [1, 2]])

    print("Matrix A:")
    print(A)

    eigenvalues, eigenvectors = eigenvalues_and_vectors(A)

    print("\nEigenvalues:")
    print(eigenvalues)

    print("\nEigenvectors (columns):")
    print(eigenvectors)
