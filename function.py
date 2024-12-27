def greet(name): #Parameters
    print(f"Hello, {name}!")
greet("Alice") #Arguments:

#Positional Arguments:
def add(a, b):
    return a + b

result = add(3, 5)  # Here, 3 is assigned to `a`, and 5 is assigned to `b`

#Keyword Arguments:
def greet(name, message):
    print(f"{message}, {name}!")

greet(message="Hello", name="Alice")

#Default Arguments:
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Alice")  # Output: Hello, Alice!

#Variable Length Positional Arguments (*args):
def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_all(1, 2, 3))  # Output: 6

#Variable Length Keyword Arguments (**kwargs):
def print_info(**kwargs):
   
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="Wonderland")

