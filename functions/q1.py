# WAP to calculate area of rectanble using function.

def area(length, breadth): # Function to calculate area of rectangle
    return length * breadth

l = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))

result = area(l, b) # Call the function and store the result
print(f"The area of the rectangle is: {result}")