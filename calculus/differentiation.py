from sympy import symbols, diff, sin, cos, exp, log, tan, simplify
from sympy.parsing.sympy_parser import parse_expr

x = symbols('x')

def differentiate_expression(expr_str, variable='x'):
    """
    Differentiate a mathematical expression with respect to a variable.

    Args:
        expr_str (str): The expression to differentiate, as a string.
        variable (str): The variable to differentiate with respect to (default is 'x').

    Returns:
        sympy expression: The derivative of the input expression.
    """
    try:
        var = symbols(variable)
        expr = parse_expr(expr_str)
        derivative = diff(expr, var)
        return simplify(derivative)
    except Exception as e:
        return f"Error in differentiation: {e}"

# Example usage
if __name__ == "__main__":
    examples = [
        "x**2 + 3*x + 2",
        "sin(x)",
        "cos(x)*x**2",
        "exp(x) + log(x)",
        "x**5 + 2*x**3 - 3*x + 1",
        "tan(x)"
    ]

    for expr in examples:
        result = differentiate_expression(expr)
        print(f"d/dx of {expr} = {result}")
