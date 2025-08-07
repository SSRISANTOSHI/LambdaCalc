from sympy import symbols, limit, sin, cos, exp, oo
from sympy.parsing.sympy_parser import parse_expr

def compute_limit(expr_str, var_str='x', point=0, direction="+"):
    """
    Compute the limit of an expression as the variable approaches a point.

    Args:
        expr_str (str): The expression (string) whose limit is to be evaluated.
        var_str (str): The variable (default 'x').
        point (float or 'oo' or '-oo'): The point the variable is approaching.
        direction (str): '+' for right-hand limit, '-' for left-hand limit, or '' for both sides.

    Returns:
        sympy expression: The result of the limit.
    """
    try:
        var = symbols(var_str)
        expr = parse_expr(expr_str)
        if point == "oo":
            point = oo
        elif point == "-oo":
            point = -oo
        return limit(expr, var, point, dir=direction)
    except Exception as e:
        return f"Error computing limit: {e}"

# Example usage
if __name__ == "__main__":
    examples = [
        ("sin(x)/x", "x", 0),
        ("(1 + 1/x)**x", "x", "oo"),
        ("(x**2 - 1)/(x - 1)", "x", 1),
        ("(x + 2)/(x**2 - 4)", "x", 2),
        ("(1/x)", "x", 0, "+"),
        ("(1/x)", "x", 0, "-")
    ]

    print("Limit Calculations:")
    for expr, var, point, *opt_dir in examples:
        dirn = opt_dir[0] if opt_dir else ""
        result = compute_limit(expr, var, point, dirn)
        print(f"lim {var}→{point}{'^' + dirn if dirn else ''} of {expr} = {result}")

