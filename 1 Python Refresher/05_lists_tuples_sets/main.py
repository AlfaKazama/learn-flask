list = ["BOB", "Rolf", "Anne"]

# you can't modify tuple, whereas you can add and remove element from a list, in tuple you can't add and remove element
tuple = ("BOB", "Rolf", "Anne")

# in set you can't have duplicate elements ,list and tuples keep the order of the elements. But sets don't necessarily keep the order
set = {"BOB", "Rolf", "Anne", "Rolf"}

print(list)
print(tuple)
print(set)

print(list[0])
print(tuple[0])


## Replace value in list, in tuple you cannot be modified after they're created 
list[0] = "Smith"
print(list)

## Add element in list, you cannot do this in tuple because tuple not allowed add and remove element
list.append("Smith")
print(list)

## Remove element in list
list.remove("Smith")
print(list)

## Add element in set
set.add("Smith")
print(set)