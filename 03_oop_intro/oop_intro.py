from abc import ABC, abstractmethod


class Student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self._grades = []
        self.__secret = "hidden"  # becomes _Student__secret

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        try:
            self._id = int(value)
        except (TypeError, ValueError):
            raise ValueError(f"invalid student id: {value!r}")

    def add_grade(self, grade):
        if not 0 <= grade <= 20:
            raise ValueError("grade must be between 0 and 20")
        self._grades.append(grade)

    @property
    def average(self):
        if not self._grades:
            raise ValueError("no grades yet")
        return sum(self._grades) / len(self._grades)

    def compute_cafet_id(self):
        return self.id + 42

    def __str__(self):
        return f"Student(id={self.id}, name={self.name})"

    def __repr__(self):
        return f"Student({self.id!r}, {self.name!r})"


class FirstYearStudent(Student):
    def __init__(self, student_id, name, major):
        super().__init__(student_id, name)
        self.major = major

    def __str__(self):
        return f"FirstYearStudent(id={self.id}, name={self.name}, major={self.major})"


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Sound made by the animal"


class Dog(Animal):
    def make_sound(self):
        return "Bark"


class Mammal(Animal):
    def __init__(self, name, age, fur_type):
        super().__init__(name, age)
        self.fur_type = fur_type


class Cat(Mammal):
    def __init__(self, name, age, fur_type, meow):
        super().__init__(name, age, fur_type)
        self.meow = meow


class Shape:
    def __init__(self, width, height, **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Color:
    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        self.color = color


class ColoredRectangle(Shape, Color):
    def __init__(self, width, height, color):
        super().__init__(width=width, height=height, color=color)


class A:
    def who(self):
        return "A"


class B(A):
    def who(self):
        return "B"


class C(A):
    def who(self):
        return "C"


class D(B, C):
    pass


class BankAccount(ABC):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    @abstractmethod
    def withdraw(self, amount):
        pass


class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        self.balance -= amount


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self * scalar

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __len__(self):
        return 2

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


if __name__ == "__main__":
    student = FirstYearStudent("2", "John", "Math")
    student.add_grade(14)
    student.add_grade(16)
    print(student, student.average)

    for animal in (Animal("Rex", 3), Dog("Rufus", 5), Cat("Tom", 2, "short", "meow")):
        print(animal.make_sound())

    rectangle = ColoredRectangle(3, 4, "blue")
    print(rectangle.area(), rectangle.color)
    print([cls.__name__ for cls in ColoredRectangle.__mro__])
    print(D().who())

    account = SavingsAccount("Melchior", 100)
    account.deposit(50)
    print(account.balance)

    v = Vector(1, 2)
    print(v + Vector(3, 4), 2 * v, len(v))
