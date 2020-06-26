"""
26) Python program to insert a given string at the beginning of all items in
a list.
"""
sampleList = []
newList = []
sizeOfSampleList = int(input("Enter number of elements in a list:"))
while sizeOfSampleList <= 0:
    sizeOfSampleList = int(input("Invalid Input.Please enter again:"))
for i in range(0, sizeOfSampleList):
    print("Enter element no.", i, ":")
    inputElement = int(input())
    sampleList.append(inputElement)
addString = str(input("Enter string to be added infront of the list:"))
for num in sampleList:
    num = addString + str(num)
    newList.append(num)
print("Given List:", sampleList)
print("Given String:", addString)
print("New List:", newList)

"""
27) Python program to replace the last element in a list with another list.
"""
sampleList27 = []
sampleList27b = []
replacedList = []
sizeOfSampleList27 = int(input("Enter number of elements in 1st list:"))
while sizeOfSampleList27 <= 0:
    sizeOfSampleList27 = int(input("Invalid Input.Please enter again:"))
for i in range(0, sizeOfSampleList27):
    print("Enter element no.", i, ":")
    inputElement = int(input())
    sampleList27.append(inputElement)

# Input for 2nd list
sizeOfSampleList27b = int(input("Enter number of elements in 2nd list:"))
while sizeOfSampleList27b <= 0:
    sizeOfSampleList27b = int(input("Invalid Input.Please enter again:"))
for i in range(0, sizeOfSampleList27b):
    print("Enter element no.", i, ":")
    inputElement = int(input())
    sampleList27b.append(inputElement)

# Actual Logic
for i in range(0, sizeOfSampleList27 - 1):
    replacedList.append(sampleList27[i])

for i in sampleList27b:
    replacedList.append(i)

print("First List:", sampleList27)
print("Second List:", sampleList27b)
print("Replaced List:", replacedList)

"""
28) Python script to add a key to a dictionary.
"""
dictSample = {0: 10, 1: 20}
print("Current dictionary:", dictSample)
choice = "Y"
while (choice == "Y"):
    key = int(input("Enter a dictionary key:"))
    value = int(input("Enter a dictionary value:"))
    dictSample.update({key: value})
    print("Updated dictionary:", dictSample)
    choice = str(input("Do you want to add an key value pair? Y/N:")).upper()

"""
29) Python script to concatenate following dictionaries to create a new one.
"""
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
newDict = {}
for i in dic1:
    j = dic1.get(i)
    newDict.update({i: j})
for i in dic2:
    j = dic2.get(i)
    newDict.update({i: j})
for i in dic3:
    j = dic3.get(i)
    newDict.update({i: j})
print("Combined dictionary:", newDict)

"""
30) Python script to check whether a given key already exists in a dictionary.
"""
sampleDict = {0: 'a', 1: 'b', 2: 'c'}
keyToCheck = int(input("Enter key to check:"))
print("Existing Dictionary:",sampleDict)
if keyToCheck in sampleDict.keys():
    print("Key already exists.")
else:
    print("Key is unique and does not exist.")
