import numpy as np

def dot_product(v1, v2):
    """
    Compute the dot product of two vectors.

    Parameters:
        v1, v2 (array-like): Input vectors.

    Returns:
        float: The dot product.
    """
    v1 = np.array(v1)
    v2 = np.array(v2)
    return np.dot(v1, v2)

def is_orthogonal(v1, v2, tol=1e-10):
    """
    Check if two vectors are orthogonal.

    Parameters:
        v1, v2 (array-like): Input vectors.
        tol (float): Tolerance level for floating point comparison.

    Returns:
        bool: True if orthogonal, False otherwise.
    """
    return abs(dot_product(v1, v2)) < tol

def norm(v):
    """
    Compute the Euclidean norm (magnitude) of a vector.

    Parameters:
        v (array-like): Input vector.

    Returns:
        float: Norm of the vector.
    """
    v = np.array(v)
    return np.linalg.norm(v)

def projection(u, v):
    """
    Project vector u onto vector v.

    Parameters:
        u, v (array-like): Input vectors.

    Returns:
        ndarray: Projection of u onto v.
    """
    u = np.array(u)
    v = np.array(v)
    v_norm_squared = np.dot(v, v)
    if v_norm_squared == 0:
        raise ValueError("Cannot project onto the zero vector.")
    return (np.dot(u, v) / v_norm_squared) * v

# Example usage
if __name__ == "__main__":
    a = [1, 2]
    b = [-2, 1]

    print("Dot product:", dot_product(a, b))
    print("Are orthogonal?", is_orthogonal(a, b))
    print("Norm of a:", norm(a))
    print("Projection of a onto b:", projection(a, b))
