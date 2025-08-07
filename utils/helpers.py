import math
import cmath
import numpy as np
from fractions import Fraction
from sympy import simplify, nsimplify, sympify

def is_number(x):
    """
    Check if x is a real or complex number.
    """
    return isinstance(x, (int, float, complex, Fraction))

def is_vector(v):
    """
    Check if input is a 1D list or NumPy array of numbers.
    """
    return isinstance(v, (list, np.ndarray)) and all(is_number(x) for x in v)

def is_matrix(m):
    """
    Check if input is a 2D list or NumPy array of numbers.
    """
    return isinstance(m, (list, np.ndarray)) and all(is_vector(row) for row in m)

def flatten_matrix(matrix):
    """
    Flatten a 2D matrix into a 1D list.
    """
    return [item for row in matrix for item in row]

def gcd(a, b):
    """
    Compute the GCD using Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """
    Compute the Least Common Multiple.
    """
    return abs(a * b) // gcd(a, b)

def round_float(x, decimals=4):
    """
    Round a float or complex number to fixed decimals.
    """
    if isinstance(x, complex):
        return complex(round(x.real, decimals), round(x.imag, decimals))
    return round(x, decimals)

def to_fraction(x):
    """
    Convert float to exact Fraction (if possible).
    """
    if isinstance(x, float):
        return Fraction(x).limit_denominator()
    return x

def simplify_expr(expr):
    """
    Simplify a symbolic expression using SymPy.
    """
    try:
        return simplify(nsimplify(expr))
    except:
        return expr

def safe_eval(expr):
    """
    Safely evaluate a simple arithmetic expression using SymPy.
    Example: "2 + 3 * (4 - 1)"
    """
    try:
        return float(sympify(expr))
    except:
        return None
