# Greeting someone
# def greet():
#     print("Hello Coder, Max!!")

# greet()


# def greet():
#     print("Hello Coder, Max!!")

# Generalised coding
# def greet(name): # <------- parameter
#     print(f"Hello Coder, {name}")

# greet("Aamod")

# Multiple paramaters example
def greet(fname, lname): # <------- parameter
    print(f"Hello Coder, {fname} {lname}")

greet("Max", "Fury")

# Positional Arguments Example
def subtract(a, b):
    difference = a - b
    return difference

result = subtract(4, 3)

print(result)

# Default arguments example (b = 1)
def subtract(a, b=1):
    difference = a - b
    return difference

result = subtract(4, 3)

print(result)

# Keyword Arguments Example
def subtract(a, b=1):
    difference = a - b
    return difference

result = subtract(b=4, a=3)

print(result)