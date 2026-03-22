# Error handling

print("This is an error handling example.")
try:
    # This will raise a ZeroDivisionError
    # print ("I am runnning!")
    result = 10 / 2
    print(f"The result is: {result}")
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero.")
    print(f"Details: {e}")
finally:
    print("This will always be executed, regardless of whether an error occurred or not.")
