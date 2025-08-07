from sympy import isprime, primerange, primefactors

def check_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if prime, False otherwise.
    """
    return isprime(n)

def generate_primes(start, end):
    """
    Generate all prime numbers in a given range [start, end).

    Args:
        start (int): Start of the range (inclusive).
        end (int): End of the range (exclusive).

    Returns:
        list: List of prime numbers in the range.
    """
    return list(primerange(start, end))

def get_prime_factors(n):
    """
    Get the list of prime factors of a number.

    Args:
        n (int): The number to factor.

    Returns:
        list: List of prime factors.
    """
    return primefactors(n)

# Example usage
if __name__ == "__main__":
    num = 97
    print(f"Is {num} a prime? {check_prime(num)}")

    print("\nPrimes between 10 and 50:")
    print(generate_primes(10, 50))

    num = 360
    print(f"\nPrime factors of {num}:")
    print(get_prime_factors(num))
