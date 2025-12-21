# Write a program to print all even numbers between 1 and 20.
e = 2
while e<=20:
    print(e)
    e = e + 2
    
# Write a program that keeps asking the user for a password until they enter "Python123".

password = ""
while password != "Python123":
    password = input("Enter the password: ")
print("Access granted!")

# Create a program to print numbers from 1 to 10 (for loop), then reverse-count from 10 to 1 (while loop).

# For loop to print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# While loop to reverse-count from 10 to 1
n = 10
while n >= 1:  
    print(n)
    n = n - 1