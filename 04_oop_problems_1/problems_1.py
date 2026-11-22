import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Account:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        return f"{self.title} by {self.author}, {self.pages} pages"


class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def play(self):
        print(f"Playing the movie {self.title}...")


if __name__ == "__main__":
    print(Rectangle(4, 5).area())
    print(round(Circle(3).area(), 2))
    print(Book("Dune", "Frank Herbert", 412).info())
    Movie("Alien", "Ridley Scott", 1979).play()

    account = Account(100)
    account.deposit(50)
    account.withdraw(30)
    print(account.balance)
