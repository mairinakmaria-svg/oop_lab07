class ZeroDivisionError(Exception):
    """Помилка створення раціонального числа зі знаменником 0."""

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        super().__init__(f"Invalid rational number {numerator}/{denominator}: denominator is zero")


class RationalError(ZeroDivisionError):
    """Виняток для некоректного створення об'єкта Rational."""

    def __init__(self, numerator, denominator):
        super().__init__(numerator, denominator)


class RationalValueError(Exception):
    """Виняток для некоректних значень під час операцій з раціональними числами."""

    def __init__(self, value, operation="operation"):
        self.value = value
        self.operation = operation
        super().__init__(f"Invalid value for {operation}: {value}")


def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a


class Rational:
    def __init__(self, numerator, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise RationalValueError((numerator, denominator), "creating Rational")

        if denominator == 0:
            raise RationalError(numerator, denominator)

        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        divider = gcd(numerator, denominator)
        self.numerator = numerator // divider
        self.denominator = denominator // divider

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return str(self)

    def _check_other(self, other, operation):
        if isinstance(other, Rational):
            return other
        if isinstance(other, int):
            return Rational(other)
        raise RationalValueError(other, operation)

    def __add__(self, other):
        other = self._check_other(other, "addition")
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __sub__(self, other):
        other = self._check_other(other, "subtraction")
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __mul__(self, other):
        other = self._check_other(other, "multiplication")
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        other = self._check_other(other, "division")
        if other.numerator == 0:
            raise RationalValueError(other, "division")
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other):
        if not isinstance(other, Rational):
            return False
        return self.numerator == other.numerator and self.denominator == other.denominator
