thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["brand"]) # Ford


print(thisdict.keys())
print(thisdict.values())

thisdict["color"] = "red"
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  
