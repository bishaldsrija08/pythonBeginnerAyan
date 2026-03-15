thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.pop("model")
print(thisdict) # {'brand': 'Ford', 'year': 1964}

del thisdict["year"]
print(thisdict) # {'brand': 'Ford'}

thisdict.clear()
print(thisdict) # {}

