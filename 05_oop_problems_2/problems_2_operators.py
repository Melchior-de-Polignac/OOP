import math


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __eq__(self, other):
        if not isinstance(other, ComplexNumber):
            return NotImplemented
        return (self.real, self.imag) == (other.real, other.imag)

    def __repr__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"({self.real} {sign} {abs(self.imag)}i)"


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return self.age > other.age


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def distance(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return math.isclose(self.distance, other.distance)

    def __lt__(self, other):
        return self.distance < other.distance


class Matrix:
    def __init__(self, rows):
        if not rows or any(len(row) != len(rows[0]) for row in rows):
            raise ValueError("rows must be non-empty and of equal length")
        self.rows = rows

    def __mul__(self, other):
        if len(self.rows[0]) != len(other.rows):
            raise ValueError("inner dimensions do not match")
        columns = list(zip(*other.rows))
        return Matrix(
            [
                [sum(a * b for a, b in zip(row, col)) for col in columns]
                for row in self.rows
            ]
        )

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        return self.rows == other.rows

    def __repr__(self):
        return f"Matrix({self.rows})"


if __name__ == "__main__":
    print(ComplexNumber(1, 2) + ComplexNumber(3, -4))
    print(Person("Ana", 30) > Person("Bob", 25))
    print(Vector(1, 2, 3) * Vector(4, 5, 6))
    print(Circle(2) < Circle(3), Circle(2) == Circle(2))
    print(Point(3, 4) < Point(1, 1))
    print(Matrix([[1, 2], [3, 4]]) * Matrix([[5, 6], [7, 8]]))
