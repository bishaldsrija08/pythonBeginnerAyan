num = 10
denom = 0
try:
    result = num / denom
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")