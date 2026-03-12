set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

# set3 = set1 | set2 # set3 = set1.union(set2) # alternative way to do the same thing
set5 = set1.union(set2, set3, set4) # we can also join more than 2 sets at the same time
print(set5)