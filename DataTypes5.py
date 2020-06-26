"""
21) Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples
"""
tupleList = []
sizeOfList = int(input("Enter number of elements in a list:"))
print("Note: If you want tuple as (1,2), enter '12' without anything in middle.")
for i in range(0, sizeOfList):
    print("Enter tuple no.", i, ":")
    inputTuple = tuple(input())
    tupleList.append(inputTuple)


def last(n):
    return n[-1]


print("Given list:", tupleList)
newList = sorted(tupleList, key=last)  # calls all the tuples in list one by one and gets the last value.
print(newList)

"""
22)Python program to remove duplicates from a list.
"""
sampleList = []
sizeOfSampleList = int(input("Enter number of elements in a list:"))
while sizeOfSampleList <= 0:
    sizeOfSampleList = int(input("Invalid Input.Please enter again:"))
for i in range(0, sizeOfSampleList):
    print("Enter element no.", i, ":")
    inputElement = input()
    sampleList.append(inputElement)
revisedSampleList = list(set(sampleList))
print("Given List:", sampleList)
print("List with unique elements:", revisedSampleList)

"""
23) Python program to check a list is empty or not.
"""
sampleList2 = []
sizeOfSampleList2 = int(input("Enter number of elements in a list:"))
for i in range(0, sizeOfSampleList2):
    print("Enter element no.", i, ":")
    userInput = input()
    sampleList.append(userInput)
if not sampleList2:
    print("List is empty.")
else:
    print("List is not empty.")

"""
24) Python program to clone or copy a list.
"""
sampleList3 = []
sizeOfSampleList3 = int(input("Enter number of elements in a list:"))
for i in range(0, sizeOfSampleList3):
    print("Enter element no.", i, ":")
    userInput = input()
    sampleList3.append(userInput)
newList = sampleList3.copy()
print("Given List:", sampleList3)
print("Copied List:", newList)

"""
25) Python program to check whether all dictionaries in a list are empty or not.
"""
dictList = [{}, {}, {}]
dictList2 = [{1, 2}, {}, {}]


def checkEmpty(dictList):
    listLength = len(dictList)
    emptyCount = 0
    for i in dictList:
        if not i:
            emptyCount += 1
    if emptyCount == listLength:
        print(True)
    else:
        print(False)


checkEmpty(dictList)
checkEmpty(dictList2)
