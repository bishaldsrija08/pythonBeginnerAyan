

# age = 18
# if age>=18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")


# age =8

# if age>18: #18>18 False
#     print("You are an adult.")
# elif age==18: # 18 ==18 True
#     print("You just became an adult.")
# else:  
#     print("You are a minor.")

# WAP to check whether a number is positive, negative or zero
# num>0 positive
# num <0 negative
# num ==0 zero

# num = int(input("Enter a number: "))

# if num>0: # num = 10, 10>0 True
#     print("The number is positive.")
# elif num<0: # 0<0 False
#     print("The number is negative.")
# else:
#     print("The number is zero.")

age = 90

if age>=18 and age<25: # 1 and 0 = 0, False
    print("You are a young adult.")
elif age>=25 and age<60: # 1 and 0 = 0, False
    print("You are an adult.")
else:
    print("You are a senior citizen.")