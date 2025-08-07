class RingElement:
    def __init__(self, value, ring):
        self.value = value
        self.ring = ring

    def __add__(self, other):
        if self.ring != other.ring:
            raise ValueError("Elements must belong to the same ring")
        return RingElement(self.ring.add(self.value, other.value), self.ring)

    def __mul__(self, other):
        if self.ring != other.ring:
            raise ValueError("Elements must belong to the same ring")
        return RingElement(self.ring.mul(self.value, other.value), self.ring)

    def __neg__(self):
        return RingElement(self.ring.neg(self.value), self.ring)

    def __sub__(self, other):
        return self + (-other)

    def __eq__(self, other):
        return self.ring == other.ring and self.value == other.value

    def __repr__(self):
        return f"{self.value} in {self.ring.name}"


class IntegerModRing:
    def __init__(self, modulus):
        if modulus <= 0:
            raise ValueError("Modulus must be a positive integer")
        self.modulus = modulus
        self.name = f"ℤ/{modulus}ℤ"

    def add(self, a, b):
        return (a + b) % self.modulus

    def mul(self, a, b):
        return (a * b) % self.modulus

    def neg(self, a):
        return (-a) % self.modulus

    def __eq__(self, other):
        return isinstance(other, IntegerModRing) and self.modulus == other.modulus

    def __repr__(self):
        return self.name


# Example usage:
if __name__ == "__main__":
    Z5 = IntegerModRing(5)
    a = RingElement(2, Z5)
    b = RingElement(3, Z5)

    print("a + b =", a + b)        # 0 in ℤ/5ℤ
    print("a * b =", a * b)        # 1 in ℤ/5ℤ
    print("-a =", -a)              # 3 in ℤ/5ℤ
    print("a - b =", a - b)        # 4 in ℤ/5ℤ
