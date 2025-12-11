# Syntax of if statement in Python
# if condition:
#      code to be executed if condition is true

b = 4
a = 5
if a > b:
    # string formatting - f-string
    print(f"{a} is greater than {b}.")

#  = means assignment
# == means comparison
if a == b:
    print(f"{a} is equal to {b}.")
    
    
    
number = 10
if number > 0:
    print(f"{number} is a positive number.")

age = int(input("Enter your age: "))
if age>=16:
    print("You are eligible to get citizenship.")