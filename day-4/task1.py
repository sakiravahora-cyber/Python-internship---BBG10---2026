import functools
import time
# 1. build_invoice using normal parameter, *args, and **kwargs
def build_invoice(customer_name, *prices, **details):
    print(f"1. Invoice for: {customer_name}")
    print(f"   Total Item Price: Rs. {sum(prices)}")
    print("   Extra Details:")
    for key, value in details.items():
        print(f"     - {key}: {value}")

build_invoice("Sakira", 250, 400, 150, discount="10%", tax="5%", payment_mode="UPI")

# 2. apply_discount with default parameter and keyword argument call
def apply_discount(price, percent=10):
    final_price = price - (price * percent / 100)
    return final_price

print("2. Default discount (10%):", apply_discount(1000))
print("   Custom discount (25%):", apply_discount(1000, percent=25))

# 3. Convert Celsius list to Fahrenheit using map() and lambda
celsius_temps = [0, 20, 30, 37, 100]
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
print("3. Fahrenheit temperatures:", fahrenheit_temps)

# 4. Filter usernames with at least 6 characters using filter() and lambda
usernames = ["riya", "sakira_v", "aman", "python_dev", "sara99", "kabir"]
valid_usernames = list(filter(lambda u: len(u) >= 6, usernames))
print("4. Valid usernames (6+ chars):", valid_usernames)

# 5. Find largest number using functools.reduce() without max()
numbers = [45, 89, 12, 95, 67, 34]
largest_num = functools.reduce(lambda a, b: a if a > b else b, numbers)
print("5. Largest number:", largest_num)

# 6. Recursive function for sum of numbers from 1 to n
def recursive_sum(n):
    if n <= 1:
        return n
    return n + recursive_sum(n - 1)

print("6. Recursive sum (1 to 10):", recursive_sum(10))

# 7. Decorator 'timer' to measure execution time in seconds
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"7. Execution time of {func.__name__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@timer
def sum_million():
    return sum(range(1, 1000001))

print("   Sum result:", sum_million())

# 8. Decorator 'require_positive' to validate positive arguments
def require_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg <= 0:
                print(f"8. Error: All arguments must be positive numbers! Invalid input: {arg}")
                return None
        return func(*args, **kwargs)
    return wrapper

@require_positive
def divide(a, b):
    return a / b

print("8. Valid divide(20, 4):", divide(20, 4))
divide(20, 0)
divide(-5, 2)