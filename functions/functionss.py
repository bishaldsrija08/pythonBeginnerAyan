"""
Functions are those that perform specific tasks and can be reused throughout the code.

They help in organizing code, improving readability, and reducing redundancy(Duplication).

Examples of functions include mathematical operations, string manipulations, data processing tasks, etc.

Types of Functions:
1. Built-in Functions: These are pre-defined functions provided by the programming language (e.g., print(), len(), type() in Python).

2. User-defined Functions: These are functions created by the user to perform specific tasks.

3. Anonymous Functions: Also known as lambda functions, these are small, unnamed functions defined using the lambda keyword in Python.

Syntax for Defining a Function in Python:
def function_name(parameters):
    # function body
    return value
"""

# Example of a User-defined Function

# Function with no parameters and no return value

def greet(): # Defining the function
    print("Hello, welcome to the world of functions!")
greet() # Calling the function

# Function with parameters and no return value
def add (a,b):
    sum = a + b
    print("The sum is:", sum)

add(5, 10) # Calling the function with arguments

# Function with parameters and return value
def multiply(x,y):
    return x * y

result = multiply(9,9) # Calling the function with arguments
print("The product is:", result)    