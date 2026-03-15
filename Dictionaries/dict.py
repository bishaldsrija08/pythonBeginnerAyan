# key: value pairs
thisdict  = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "name": "Bishal",
    "colors": ["red", "green", "blue"]
}

print(thisdict) # {'name': 'Bishal', 'age': 30, 'city': 'New York', 'colors': ['red', 'green', 'blue']}


print(thisdict["name"]) # Bishal
print(thisdict.get("name")) # Bishal

print(len(thisdict)) # 3

print(type(thisdict)) # <class 'dict'>


for x in thisdict:
    print(thisdict[x]) # Bishal 30 New York ['red', 'green', 'blue']