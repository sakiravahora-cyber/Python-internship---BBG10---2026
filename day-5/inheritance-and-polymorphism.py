#1
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def _init_(self, name, age, course):
        super()._init_(name, age)
        self.course = course

    def study(self):
        print(f"{self.name} (age {self.age}) is studying {self.course}.")


student = Student("Sakira", 20, "BCA")
student.study()

#2
class Employee:
    def _init_(self, name, base_salary=30000):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Developer(Employee):
    def _init_(self, name, base_salary=30000, project_bonus=8000):
        super()._init_(name, base_salary)
        self.project_bonus = project_bonus

    def calculate_salary(self):
        return super().calculate_salary() + self.project_bonus


class Designer(Employee):
    def _init_(self, name, base_salary=30000, design_bonus=5000):
        super()._init_(name, base_salary)
        self.design_bonus = design_bonus

    def calculate_salary(self):
        return super().calculate_salary() + self.design_bonus


dev = Developer("Rohan")
des = Designer("Meera")

print("Developer Salary:", dev.calculate_salary())
print("Designer Salary:", des.calculate_salary())

#3
class Account:
    def get_interest_rate(self):
        return 4


class SavingsAccount(Account):
    def get_interest_rate(self):
        return 5.5


class FixedDeposit(Account):
    def get_interest_rate(self):
        return 7.2


accounts = [Account(), SavingsAccount(), FixedDeposit()]

for acc in accounts:
    print(f"{type(acc)._name_} interest rate: {acc.get_interest_rate()}%")
    
#4
class Bird:
    def fly(self):
        print("Bird flaps its wings and flies in the sky.")


class Airplane:
    def fly(self):
        print("Airplane takes off down the runway and flies high.")


class Drone:
    def fly(self):
        print("Drone lifts off using four rotors.")


def start_flight(flying_object):
    flying_object.fly()


start_flight(Bird())
start_flight(Airplane())
start_flight(Drone())

#5
class Vehicle:
    def _init_(self, brand):
        self.brand = brand


class Car(Vehicle):
    def _init_(self, brand, model):
        super()._init_(brand)
        self.model = model


class SportsCar(Car):
    def _init_(self, brand, model, top_speed):
        super()._init_(brand, model)
        self.top_speed = top_speed

    def show_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Top Speed: {self.top_speed} km/h")


sc = SportsCar("Ferrari", "F8 Tributo", 340)
sc.show_details()

#6
class Notification:
    def send(self):
        print("Sending a generic notification.")


class EmailNotification(Notification):
    def _init_(self, recipient):
        self.recipient = recipient

    def send(self):
        print(f"Sending Email notification to {self.recipient}.")


class SMSNotification(Notification):
    def _init_(self, phone_number):
        self.phone_number = phone_number

    def send(self):
        print(f"Sending SMS notification to {self.phone_number}.")


notifications = [
    Notification(),
    EmailNotification("user@example.com"),
    SMSNotification("+91-9876543210"),
]

for note in notifications:
    note.send()