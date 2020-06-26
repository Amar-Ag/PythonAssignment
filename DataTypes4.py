"""
16) Python program to sum all the items in a list.
"""
sampleList = []
sizeOfList = int(input("Enter number of elements in a list:"))
for i in range(0, sizeOfList):
    print("Enter element no.", i, ":")
    inputNumber = int(input())
    sampleList.append(inputNumber)
print("Given List:", sampleList)
print("Sum of the given list:", sum(sampleList))

"""
17) Python program to multiplies all the items in a list
"""
sampleList2 = []
productList = 1
sizeOfList2 = int(input("Enter number of elements in a list:"))
for i in range(0, sizeOfList2):
    print("Enter element no.", i, ":")
    inputNumber = int(input())
    sampleList2.append(inputNumber)
    productList *= inputNumber
print("Given List:", sampleList2)
print("Product of the given list:", productList)

"""
18) Python program to get the largest number from a list.
"""
sampleList3 = []
sizeOfList3 = int(input("Enter number of elements in a list:"))
for i in range(0, sizeOfList3):
    print("Enter element no.", i, ":")
    inputNumber = int(input())
    sampleList3.append(inputNumber)
greaterInList = sampleList3[0]
for i in sampleList3:
    if greaterInList < i:
        greaterInList = i

print("Given List:", sampleList3)
print("Greatest number of the given list:", greaterInList)

"""
19) Python program to get the smallest number from a list.
"""
sampleList4 = []
sizeOfList4 = int(input("Enter number of elements in a list:"))
for i in range(0, sizeOfList4):
    print("Enter element no.", i, ":")
    inputNumber = int(input())
    sampleList4.append(inputNumber)
smallerInList = sampleList4[0]
for i in sampleList4:
    if smallerInList > i:
        smallerInList = i

print("Given List:", sampleList4)
print("Smallest number of the given list:", smallerInList)

"""
20) Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given list of
strings.
"""
stringList = []
matchCount = 0
sizeOfStringList = int(input("Enter number of elements in a list:"))
for i in range(0, sizeOfStringList):
    print("Enter element no.", i, ":")
    inputString = str(input())
    stringList.append(inputString)
for i in stringList:
    if len(i) >= 2 and i[0] == i[-1]:
        matchCount += 1
print("Given list:", stringList)
print("Number of string in list matching the criteria:", matchCount)
