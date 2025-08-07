from sympy import mod_inverse
from math import gcd
from functools import reduce

def mod_add(a, b, m):
    """
    Perform modular addition.

    (a + b) mod m
    """
    return (a + b) % m

def mod_sub(a, b, m):
    """
    Perform modular subtraction.

    (a - b) mod m
    """
    return (a - b) % m

def mod_mul(a, b, m):
    """
    Perform modular multiplication.

    (a * b) mod m
    """
    return (a * b) % m

def mod_inv(a, m):
    """
    Compute modular inverse using sympy.

    Returns the inverse of a mod m if it exists.
    """
    try:
        return mod_inverse(a, m)
    except ValueError:
        return None  # Inverse doesn't exist

def chinese_remainder_theorem(remainders, moduli):
    """
    Solve system of congruences using the Chinese Remainder Theorem.

    Args:
        remainders (list): List of remainders.
        moduli (list): List of pairwise co-prime moduli.

    Returns:
        int: The smallest x satisfying all congruences.
    """
    if len(remainders) != len(moduli):
        raise ValueError("Length of remainders and moduli must be equal.")

    total_mod = reduce(lambda a, b: a * b, moduli)
    result = 0

    for r_i, m_i in zip(remainders, moduli):
        partial_mod = total_mod // m_i
        inv = mod_inv(partial_mod, m_i)
        if inv is None:
            raise ValueError(f"No inverse exists for {partial_mod} mod {m_i}")
        result += r_i * partial_mod * inv

    return result % total_mod

# Example usage
if __name__ == "__main__":
    a, b, m = 7, 5, 12
    print(f"({a} + {b}) % {m} = {mod_add(a, b, m)}")
    print(f"({a} * {b}) % {m} = {mod_mul(a, b, m)}")
    print(f"Inverse of {a} mod {m} = {mod_inv(a, m)}")

    # CRT example
    rems = [2, 3, 2]
    mods = [3, 5, 7]
    print(f"\nCRT result for remainders {rems} and moduli {mods}: {chinese_remainder_theorem(rems, mods)}")
