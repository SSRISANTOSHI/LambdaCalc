import re
import numpy as np

def parse_vector(s):
    """
    Parse a string into a numeric vector.
    Example: "(1, 2, 3)" → [1.0, 2.0, 3.0]

    Parameters:
        s (str): Input string.

    Returns:
        list of floats
    """
    try:
        return [float(x.strip()) for x in s.strip("()[]").split(",")]
    except ValueError:
        raise ValueError("Invalid vector format. Use comma-separated values in (), [], or just numbers.")

def parse_matrix(s):
    """
    Parse a string into a matrix.
    Example: "[[1, 2], [3, 4]]" → np.array([[1, 2], [3, 4]])

    Parameters:
        s (str): Input string.

    Returns:
        numpy.ndarray
    """
    try:
        return np.array(eval(s), dtype=float)
    except Exception:
        raise ValueError("Invalid matrix format. Use Python-like nested list format, e.g., [[1,2],[3,4]].")

def parse_polynomial(s):
    """
    Parse a polynomial string into a list of coefficients.
    Example: "2x^2 + 3x - 5" → [2, 3, -5]

    Parameters:
        s (str): Polynomial string.

    Returns:
        list: Coefficients from highest to constant term.
    """
    try:
        # Remove whitespace
        s = s.replace(" ", "")
        # Add '+' before negative signs
        s = re.sub(r"(?<!^)-", "+-", s)
        terms = s.split("+")
        coeffs = {}
        for term in terms:
            if 'x^' in term:
                c, p = term.split('x^')
                power = int(p)
                coeff = float(c) if c not in ["", "+"] else 1.0
                if c == "-":
                    coeff = -1.0
            elif 'x' in term:
                power = 1
                coeff = float(term.replace("x", "")) if term.replace("x", "") not in ["", "+"] else 1.0
                if term.startswith("-x"):
                    coeff = -1.0
            else:
                power = 0
                coeff = float(term)
            coeffs[power] = coeff
        max_power = max(coeffs.keys())
        return [coeffs.get(i, 0.0) for i in reversed(range(max_power + 1))]
    except Exception:
        raise ValueError("Invalid polynomial format. Try format like: 2x^2 + 3x - 5")

# Example usage
if __name__ == "__main__":
    print("Parsed vector:", parse_vector("(1, -2, 3)"))
    print("Parsed matrix:", parse_matrix("[[1, 2], [3, 4]]"))
    print("Parsed polynomial:", parse_polynomial("2x^2 + 3x - 5"))
