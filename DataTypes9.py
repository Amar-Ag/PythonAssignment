"""
41) Python program to convert a tuple to a string
"""
sampleTuple = ("This", "is", "a", "tuple")
print("Tuple:", sampleTuple)
stringTuple = ''.join(sampleTuple)
print("As a string:", stringTuple)

"""
42) Python program to convert a list to a tuple
"""
sampleList = ["This", "is", "a", "list"]
listTuple = tuple(sampleList)
print("List:", sampleList)
print("Tuple:", listTuple)

"""
43) Python program to remove an item from a tuple
"""
sampleTuple2 = ("This", "is", "a", "tuple")
print("Existing Tuple:", sampleTuple2)
removeWord = str(input("Enter the word you want to remove:"))
sampleList2 = list(sampleTuple2)
sampleList2.remove(removeWord)
sampleTuple2 = tuple(sampleList2)
print("Updated tuple:", sampleTuple2)

"""
44) Python program to slice a tuple.
"""
newTuple = ("This", "is", "a", "new", "Python", "tuple")
print("Original tuple:", newTuple)
print("Sliced tuple:", newTuple[2:])

"""
45) Python program to find the index of an item of a tuple
"""
newTuple2 = ("This", "is", "a", "new", "Python", "tuple")
print("Existing tuple:", newTuple2)
itemValue = str(input("Enter the item whose index is to be displayed:"))
print("Index:", newTuple2.index(itemValue))

"""
46) Python program to find the length of a tuple
"""
newTuple3 = ("This", "is", "a", "new", "Python", "tuple")
print("Existing tuple:", newTuple3)
print("Length:", len(newTuple3))
