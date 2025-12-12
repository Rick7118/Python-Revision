# oop_cheatsheet.py
# ---------------------------------------
# OOP Cheatsheet — Everything in one file
#
# Short, practical, and runnable examples of OOP concepts you need:
# - classes & objects
# - __init__, self
# - instance vs class variables
# - methods
# - inheritance + super()
# - simple demos for each example (Car, Student, Employee, Calculator, ShoppingCart)
#
# Run: python oop_cheatsheet.py
# ---------------------------------------

from typing import List, Dict

# ---------------------------
# Quick conceptual notes:
#
# - A class is a blueprint; an object/instance is a concrete thing built from that blueprint.
# - `__init__(self, ...)` is the constructor: it initializes each new object.
# - `self` is the instance itself; use it to attach attributes.
# - Instance variables: stored per object (self.x).
# - Class variables: shared by all instances (defined at class level).
# - Methods are functions defined inside a class; call them on instances.
# - Inheritance: class Child(Parent): ... → Child gets Parent's methods/attributes.
# - Use `super()` to call parent methods (constructor often).
# ---------------------------


# ---------------------------
# Example 1 — Car class
# ---------------------------
class Car:
    # class variable (shared)
    wheels = 4

    def __init__(self, brand: str, year: int, running: bool = False):
        """Create a Car with brand and year. running defaults to False."""
        self.brand = brand          # instance variable
        self.year = year
        self.running = running

    def start(self):
        """Start the car."""
        if not self.running:
            self.running = True
            print(f"{self.brand} started.")
        else:
            print(f"{self.brand} is already running.")

    def stop(self):
        """Stop the car."""
        if self.running:
            self.running = False
            print(f"{self.brand} stopped.")
        else:
            print(f"{self.brand} is already stopped.")

    def info(self):
        """Return a simple string with car information."""
        return f"{self.brand} ({self.year}) - running: {self.running}"


# ---------------------------
# Example 2 — Student class
# ---------------------------
class Student:
    def __init__(self, name: str, marks: List[int] = None):
        """Student with a list of marks (ints)."""
        self.name = name
        self.marks = marks if marks is not None else []

    def add_mark(self, mark: int):
        """Add a numeric mark to the student's record."""
        self.marks.append(mark)

    def average(self) -> float:
        """Return average of marks, or 0.0 if no marks."""
        return sum(self.marks) / len(self.marks) if self.marks else 0.0

    def report(self) -> str:
        """Human readable report."""
        return f"{self.name}: avg={self.average():.2f}, marks={self.marks}"


# ---------------------------
# Example 3 — Employee class
# ---------------------------
class Employee:
    def __init__(self, name: str, salary: float):
        """Employee with name and salary."""
        self.name = name
        self.salary = salary

    def give_raise(self, amount: float):
        """Increase salary by amount (>0)."""
        if amount <= 0:
            raise ValueError("Raise amount must be positive")
        self.salary += amount

    def info(self) -> str:
        return f"{self.name}: salary={self.salary:.2f}"


# ---------------------------
# Example 4 — Calculator class
# ---------------------------
class Calculator:
    """Stateless calculator object — methods perform arithmetic and return results."""

    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


# ---------------------------
# Example 5 — ShoppingCart class
# ---------------------------
class ShoppingCart:
    def __init__(self):
        # store items as list of dicts: {"name": str, "price": float, "qty": int}
        self.items: List[Dict] = []

    def add_item(self, name: str, price: float, qty: int = 1):
        """Add an item. If exists, increase quantity."""
        if qty <= 0:
            raise ValueError("Quantity must be positive")

        for it in self.items:
            if it["name"] == name:
                it["qty"] += qty
                return
        self.items.append({"name": name, "price": price, "qty": qty})

    def remove_item(self, name: str, qty: int = 1):
        """Remove qty of item; if qty removes all, delete the item."""
        for it in self.items:
            if it["name"] == name:
                if qty >= it["qty"]:
                    self.items.remove(it)
                else:
                    it["qty"] -= qty
                return
        raise KeyError(f"Item {name} not in cart")

    def total_items(self) -> int:
        return sum(it["qty"] for it in self.items)

    def total_price(self) -> float:
        return sum(it["qty"] * it["price"] for it in self.items)

    def summary(self) -> str:
        lines = [f"{it['name']} x{it['qty']} @ {it['price']:.2f}" for it in self.items]
        return "\n".join(lines) + f"\nTotal items: {self.total_items()}, Total price: {self.total_price():.2f}"


# ---------------------------
# Example 6 — Inheritance demo (Animal / Dog)
# ---------------------------
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name)  # call parent constructor
        self.breed = breed

    def speak(self):
        print(f"{self.name} the {self.breed} says: Bark!")


# ---------------------------
# Small utilities / tests used in demo
# ---------------------------
def _demo_car():
    print("=== Car demo ===")
    c = Car("Toyota", 2019)
    print(c.info())
    c.start()
    c.start()  # starting again shows already running path
    c.stop()
    print()


def _demo_student():
    print("=== Student demo ===")
    s = Student("Anika", [85, 90])
    print(s.report())
    s.add_mark(95)
    print("After adding mark:", s.report())
    print()


def _demo_employee():
    print("=== Employee demo ===")
    e = Employee("Rohit", 50000.0)
    print(e.info())
    e.give_raise(4000.0)
    print("After raise:", e.info())
    try:
        e.give_raise(-100)  # shows error handling
    except ValueError as ex:
        print("Caught error:", ex)
    print()


def _demo_calculator():
    print("=== Calculator demo ===")
    print("add(3,4) ->", Calculator.add(3, 4))
    print("divide(10,2) ->", Calculator.divide(10, 2))
    try:
        Calculator.divide(5, 0)
    except ZeroDivisionError as ex:
        print("Caught division error:", ex)
    print()


def _demo_shopping_cart():
    print("=== ShoppingCart demo ===")
    cart = ShoppingCart()
    cart.add_item("apple", 10.0, 3)
    cart.add_item("banana", 5.0, 2)
    cart.add_item("apple", 10.0, 1)  # increases apple qty
    print(cart.summary())
    cart.remove_item("banana", 1)
    print("After removing 1 banana:")
    print(cart.summary())
    try:
        cart.remove_item("mango")
    except KeyError as ex:
        print("Caught error:", ex)
    print()


def _demo_inheritance():
    print("=== Inheritance demo ===")
    a = Animal("SomeAnimal")
    a.speak()
    d = Dog("Buddy", "Labrador")
    d.speak()
    print()


# ---------------------------
# If run directly, show demos
# ---------------------------
if __name__ == "__main__":
    print("OOP Cheatsheet — running demos\n")
    _demo_car()
    _demo_student()
    _demo_employee()
    _demo_calculator()
    _demo_shopping_cart()
    _demo_inheritance()

    print("You can import these classes in other files, e.g.:")
    print("  from oop_cheatsheet import Car, Student, ShoppingCart")
    print("Then create objects and use them in your projects.")
