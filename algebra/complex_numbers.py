import math

class Complex:
    def __init__(self, real: float = 0.0, imag: float = 0.0):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return f"({self.real} {'+' if self.imag >= 0 else '-'} {abs(self.imag)}i)"

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        if denom == 0:
            raise ZeroDivisionError("Cannot divide by zero complex number")
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(real, imag)

    def conjugate(self):
        return Complex(self.real, -self.imag)

    def modulus(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def argument(self):
        return math.atan2(self.imag, self.real)

    def polar(self):
        return (self.modulus(), self.argument())

    @staticmethod
    def from_polar(r: float, theta: float):
        return Complex(r * math.cos(theta), r * math.sin(theta))

# Example usage
if __name__ == "__main__":
    z1 = Complex(3, 4)
    z2 = Complex(1, -2)

    print("z1:", z1)
    print("z2:", z2)
    print("Addition:", z1 + z2)
    print("Subtraction:", z1 - z2)
    print("Multiplication:", z1 * z2)
    print("Division:", z1 / z2)
    print("Conjugate of z1:", z1.conjugate())
    print("Modulus of z1:", z1.modulus())
    print("Argument of z1 (radians):", z1.argument())
    print("Polar form of z1:", z1.polar())
    print("From polar (5, π/2):", Complex.from_polar(5, math.pi/2))
