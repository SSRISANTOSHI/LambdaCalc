from math import gcd

def compute_gcd(a, b):
    """
    Compute the Greatest Common Divisor (GCD) of two integers.
    """
    return gcd(a, b)

def compute_lcm(a, b):
    """
    Compute the Least Common Multiple (LCM) of two integers.
    """
    return abs(a * b) // gcd(a, b)

def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm.
    Returns a tuple of (gcd, x, y) such that:
    ax + by = gcd(a, b)
    """
    if b == 0:
        return (a, 1, 0)
    else:
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (g, x, y)

# Example usage
if __name__ == "__main__":
    a, b = 60, 48
    print(f"GCD({a}, {b}) = {compute_gcd(a, b)}")
    print(f"LCM({a}, {b}) = {compute_lcm(a, b)}")

    g, x, y = extended_gcd(a, b)
    print(f"Extended GCD of {a} and {b}: gcd = {g}, x = {x}, y = {y}")
    print(f"Check: {a}*{x} + {b}*{y} = {a*x + b*y}")
