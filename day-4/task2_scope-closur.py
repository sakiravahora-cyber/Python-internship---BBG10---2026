#1 
call_count = 0

def track_calls():
    global call_count
    call_count += 1

track_calls()
track_calls()
track_calls()
track_calls()

print("Total calls:", call_count)

#2 
def make_greeting(language):
    def greet(name):
        if language.lower() == "hindi":
            print(f"Namaste, {name}")
        else:
            print(f"Hello, {name}")
    return greet

hindi_greet = make_greeting("hindi")
english_greet = make_greeting("english")

hindi_greet("Sakira")
english_greet("Sakira")

#3
def make_counter(start):
    count = start

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter_a = make_counter(0)
counter_b = make_counter(100)

# Call counter_a 3 times
counter_a()
counter_a()
res_a = counter_a()

# Call counter_b 2 times
counter_b()
res_b = counter_b()

print("Counter A final:", res_a)
print("Counter B final:", res_b)

#4 
def process_task():
    status = "pending"

    def finish_task():
        nonlocal status
        status = "completed"

    finish_task()
    print("Final status:", status)

process_task()

mode = "Global Mode"

#5
def outer_function():
    mode = "Enclosing Mode"

    def inner_function():
        mode = "Local Mode"
        print("Inside inner_function:", mode)

    inner_function()
    print("Inside outer_function:", mode)

outer_function()
print("At module level:", mode)

#6
def make_validator(min_value):
    def is_valid(number):
        return number >= min_value
    return is_valid

adult_validator = make_validator(18)
passing_validator = make_validator(40)

print("Age 20 valid:", adult_validator(20))
print("Age 15 valid:", adult_validator(15))

print("Score 40 valid:", passing_validator(40))
print("Score 32 valid:", passing_validator(32))