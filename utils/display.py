import numpy as np

def print_vector(v, label="Vector"):
    """
    Pretty-print a vector.
    """
    v_str = ", ".join(f"{x:.2f}" for x in v)
    print(f"{label}: ({v_str})")

def print_matrix(m, label="Matrix"):
    """
    Pretty-print a matrix.
    """
    print(f"{label}:")
    for row in m:
        print("  " + "  ".join(f"{x:.2f}" for x in row))

def print_polynomial(coeffs, label="Polynomial"):
    """
    Pretty-print a polynomial from coefficient list.
    E.g., [2, 0, -3] -> "2x^2 - 3"
    """
    terms = []
    degree = len(coeffs) - 1
    for i, coeff in enumerate(coeffs):
        power = degree - i
        if abs(coeff) < 1e-10:
            continue  # skip near-zero terms
        sign = "+" if coeff > 0 else "-"
        coeff_abs = abs(coeff)

        if power == 0:
            term = f"{coeff_abs:.2f}"
        elif power == 1:
            term = f"{coeff_abs:.2f}x"
        else:
            term = f"{coeff_abs:.2f}x^{power}"

        if i == 0 and coeff > 0:
            terms.append(term)
        else:
            terms.append(f" {sign} {term}")
    
    poly_str = "".join(terms) if terms else "0"
    print(f"{label}: {poly_str.strip()}")

def print_title(title):
    """
    Print a formatted title header.
    """
    print(f"\n=== {title.upper()} ===\n")

# Example usage
if __name__ == "__main__":
    print_title("Display Demo")
    print_vector([1.23456, -2, 0], "v")
    print_matrix(np.array([[1, 2], [3.1415, 4]]), "A")
    print_polynomial([2, 0, -3], "P(x)")
