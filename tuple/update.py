mytuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")


myList = list(mytuple)
myList[1] = "blackcurrant"
mytuple = tuple(myList)

print(mytuple)