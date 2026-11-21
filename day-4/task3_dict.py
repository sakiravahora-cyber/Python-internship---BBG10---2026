#1
def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Both inputs must be numbers."

print(safe_division(10, 2))
print(safe_division(10, 0))
print(safe_division(10, "a"))

#2
def get_item_at_index(items, index):
    try:
        return items[index]
    except IndexError:
        return None

fruits = ["apple", "banana", "cherry"]
print(get_item_at_index(fruits, 1))
print(get_item_at_index(fruits, 5))

#3
class InvalidAgeError(Exception):
    pass

def register_user(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(f"Invalid age ({age}): Age must be between 0 and 120.")
    print(f"User registered successfully with age {age}.")

try:
    register_user(19)
    register_user(150)
except InvalidAgeError as e:
    print("Registration failed:", e)

#4
def read_file_safely(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"

print(read_file_safely("missing_notes.txt"))

#5
class OutOfRangeError(Exception):
    pass

while True:
    try:
        num = int(input("Enter a number between 1 and 10: "))
        if num < 1 or num > 10:
            raise OutOfRangeError("Number must be between 1 and 10.")
        print(f"Valid number entered: {num}")
        break
    except ValueError:
        print("Invalid input: Please enter a valid integer.")
    except OutOfRangeError as e:
        print("Out of range:", e)
        
#6
def process_order(order):
    try:
        item = order["item"]
        price = order["price"]
    except KeyError as missing_key:
        print(f"Error: Missing required key {missing_key} in order.")
    else:
        print(f"Order confirmed: {item} - ₹{price}")
    finally:
        print("Processing complete")

process_order({"item": "Laptop Stand", "price": 799})
print("---")
process_order({"item": "Mouse"}) 