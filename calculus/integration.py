from sympy import symbols, integrate, sin, cos, exp, log, tan
from sympy.parsing.sympy_parser import parse_expr
from sympy import sympify

x = symbols('x')

def indefinite_integral(expr_str, variable='x'):
    """
    Compute the indefinite integral of an expression.

    Args:
        expr_str (str): Expression as a string.
        variable (str): Variable to integrate with respect to (default is 'x').

    Returns:
        sympy expression: Indefinite integral.
    """
    try:
        var = symbols(variable)
        expr = parse_expr(expr_str)
        return integrate(expr, var)
    except Exception as e:
        return f"Error in indefinite integration: {e}"

def definite_integral(expr_str, a, b, variable='x'):
    """
    Compute the definite integral of an expression over [a, b].

    Args:
        expr_str (str): Expression as a string.
        a (float): Lower limit.
        b (float): Upper limit.
        variable (str): Variable to integrate with respect to (default is 'x').

    Returns:
        float or symbolic result.
    """
    try:
        var = symbols(variable)
        expr = parse_expr(expr_str)
        result = integrate(expr, (var, a, b))
        return result
    except Exception as e:
        return f"Error in definite integration: {e}"

# Example usage
if __name__ == "__main__":
    print("Indefinite Integrals:")
    exprs = ["x**2", "sin(x)", "exp(x)", "1/x"]
    for expr in exprs:
        print(f"∫ {expr} dx = {indefinite_integral(expr)}")

    print("\nDefinite Integrals from 0 to 1:")
    exprs = ["x", "x**2", "sin(x)", "exp(x)"]
    for expr in exprs:
        print(f"∫₀¹ {expr} dx = {definite_integral(expr, 0, 1)}")
