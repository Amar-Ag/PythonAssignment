"""
36) Python program to sum all the items in a dictionary.
"""
sampleDict = {0: 400, 2: 500, 3: 600}
print("Existing Dictionary:", sampleDict)
print("Sum of the dictionary:", sum(sampleDict.values()))

"""
37) Python program to multiply all the items in a dictionary
"""
sampleDict2 = {0: 400, 2: 500, 3: 600}
print("Existing Dictionary:", sampleDict2)
productDict = 1
for i in sampleDict.values():
    productDict *= i
print("Product of the list:%d" % productDict)

"""
38) Python program to remove a key from a dictionary.
"""
dictSample = {0: 10, 1: 20, 2: 30, 3: 40}
print("Current dictionary:", dictSample)
choice = "Y"
while (choice == "Y"):
    key = int(input("Enter a dictionary key to be deleted:"))
    dictSample.pop(key)
    print("Updated dictionary:", dictSample)
    choice = str(input("Do you want to delete more keys? Y/N:")).upper()

"""
39) Python program to unpack a tuple in several variables.
"""
sampleTuple = ("This", "is", "a", "tuple")
varA, varB, varC, varD = sampleTuple
print(varA, varB, varC, varD)

"""
40) Python program to add an item in a tuple
"""
sampleTuple2 = ("This", "is", "a", "tuple")
addWord = str(input("Enter the word you want to add:"))
print("Before addition:", sampleTuple2)
sampleTuple2 = sampleTuple2 + (addWord,)
print("After addition:", sampleTuple2)
