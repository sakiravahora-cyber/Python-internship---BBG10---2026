
#1
class Car:
    def _init_(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"This car is a {self.year} {self.brand} {self.model}.")


car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Honda", "Civic", 2024)
car3 = Car("Hyundai", "i20", 2021)

car1.display_info()
car2.display_info()
car3.display_info()

#2
class Counter:
    total_count = 0

    def _init_(self):
        Counter.total_count += 1

    @classmethod
    def get_total_count(cls):
        return cls.total_count


c1 = Counter()
c2 = Counter()
c3 = Counter()
c4 = Counter()
c5 = Counter()

print("Total Counter objects created:", Counter.get_total_count())

#3
import math

class Circle:
    def _init_(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @property
    def circumference(self):
        return 2 * math.pi * self.radius


circle = Circle(7)
print("Area:", circle.area)
print("Circumference:", circle.circumference)

#4
class Employee:
    def _init_(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
            print(f"Salary updated to {self.__salary}.")
        else:
            print(
                f"Invalid update: new salary ({new_salary}) cannot be less than or equal to current salary ({self.__salary})."
            )


emp = Employee("Aarav", 40000)
print("Initial Salary:", emp.get_salary())

# Valid increase
emp.set_salary(48000)
print("Current Salary:", emp.get_salary())

# Invalid decrease attempt
emp.set_salary(35000)
print("Final Salary:", emp.get_salary())

#5
class Temperature:
    def _init_(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15 C).")
        self._celsius = value

    @property
    def kelvin(self):
        return self._celsius + 273.15


temp = Temperature(25)
print("Celsius:", temp.celsius)
print("Kelvin:", temp.kelvin)

temp.celsius = 0
print("Updated Celsius:", temp.celsius)
print("Updated Kelvin:", temp.kelvin)

#6
class Rectangle:
    def _init_(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def _eq_(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.area() == other.area()


rect1 = Rectangle(4, 6)  # Area = 24
rect2 = Rectangle(3, 8)  # Area = 24

print("Rect 1 area:", rect1.area())
print("Rect 2 area:", rect2.area())
print("Are they equal by area?", rect1 == rect2)

#7
class Library:
    def _init_(self):
        self.__books = []

    def add_book(self, title):
        self.__books.append(title)
        print(f"Added '{title}' to the library.")

    def remove_book(self, title):
        if title in self.__books:
            self.__books.remove(title)
            print(f"Removed '{title}' from the library.")
        else:
            print(f"'{title}' not found in the library.")

    def list_books(self):
        # Return a shallow copy so external code cannot mutate internal list directly
        return list(self.__books)


library = Library()
library.add_book("Clean Code")
library.add_book("Python Crash Course")
library.add_book("The Pragmatic Programmer")

print("Books in library:", library.list_books())

library.remove_book("Python Crash Course")
print("Books after removal:", library.list_books())

# Trying to modify the returned list does not affect the internal __books list
external_view = library.list_books()
external_view.clear()
print("Books still in library:", library.list_books())