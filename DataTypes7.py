"""
31) Python program to iterate over dictionaries using for loops.
"""
sampleDict = {0: "Sample", 1: "Python", 2: "Dictionary"}
for i in sampleDict.items():
    print("Key:", i[0], "Value:", i[1])

"""
32) Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
"""
inputNumber = int(input("Enter a number:"))
sampleDict2 = dict()
for i in range(1, inputNumber + 1):
    sampleDict2[i] = i * i
print("Dictionary:", sampleDict2)

"""
33) Python script to print a dictionary where the keys are numbers
between 1 and 15 (both included) and the values are square of keys.
"""
sampleDict3 = dict()
for i in range(1, 16):
    sampleDict3[i] = i * i
print("Dictionary:", sampleDict3)

"""
34) Python script to merge two Python dictionaries.
"""
firstDict = {0: 'a', 1: 'b', 2: 'c'}
secondDict = {3: 'd', 4: 'e', 5: 'f'}
mergedDict = firstDict.copy()
mergedDict = mergedDict.update(secondDict)
print("First Dictionary:", firstDict)
print("Second Dictionary:", secondDict)
print("Merged Dictionary:", mergedDict)

"""
35) Python program to iterate over dictionaries using for loops
"""
sampleDict = {0: "Sample", 1: "Python", 2: "Dictionary"}
for i in sampleDict:
    print("Key:", i, "Value:", sampleDict.get(i))
