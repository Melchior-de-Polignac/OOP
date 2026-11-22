class Vehicle:
    def drive(self):
        return "Driving a vehicle"


class Car(Vehicle):
    def drive(self):
        return "Driving a car"


class Bicycle(Vehicle):
    def drive(self):
        return "Riding a bicycle"


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def introduce(self):
        return f"Hi, I am {self.name}, {self.age} years old, living at {self.address}."


class Student(Person):
    def __init__(self, name, age, address, field_of_study):
        super().__init__(name, age, address)
        self.field_of_study = field_of_study

    def introduce(self):
        return f"{super().introduce()} I study {self.field_of_study}."


class Employee(Person):
    def __init__(self, name, age, address, company):
        super().__init__(name, age, address)
        self.company = company

    def introduce(self):
        return f"{super().introduce()} I work at {self.company}."


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdrawal must be positive")
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

    def transfer(self, destination, amount):
        if amount > self.balance:
            return False
        self.withdraw(amount)
        destination.deposit(amount)
        return True


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.0):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        if interest > 0:
            self.deposit(interest)

    def check_balance(self):
        return self.balance


if __name__ == "__main__":
    for vehicle in (Vehicle(), Car(), Bicycle()):
        print(vehicle.drive())

    for person in (
        Person("Lina", 45, "Lyon"),
        Student("Yanis", 19, "Paris", "mathematics"),
        Employee("Claire", 31, "Bordeaux", "Airbus"),
    ):
        print(person.introduce())

    current = BankAccount("FR-001", 500)
    savings = SavingsAccount("FR-002", 1000, 0.03)
    current.transfer(savings, 200)
    savings.add_interest()
    print(current.balance, savings.check_balance())
