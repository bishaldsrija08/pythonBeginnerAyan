thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2020
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

thisdict.update({"year": 2021})
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', '


thisdict["offroad"] = True
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2021, 'offroad': True}