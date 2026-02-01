# WAP to find gratest of two numbers using function.

def greatest(num1, num2):  # Function to find greatest of two numbers
    if num1 > num2:
        return num1
    else:
        return num2

# Input from user
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

# Call the function and display the result
result = greatest(number1, number2)
print(f"The greatest of {number1} and {number2} is {result}.")
