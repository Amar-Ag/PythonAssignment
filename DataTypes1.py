"""
1) Python program to count the number of characters (character
frequency) in a string. Sample String : google.com
"""
sampleString = str(input("Enter a string:")) or "google.com"
sampleDict = {}
for i in sampleString:
    keys = sampleDict.keys()
    if i in keys:
        sampleDict[i] += 1
    else:
        sampleDict[i] = 1
print("Characters and their occurences in given string = ", sampleDict)

"""
2) Python program to get a string made of the first 2 and the last 2 chars
from a given a string. If the string length is less than 2, return instead of the
empty string.
"""
sampleString2 = str(input("Enter a string:")) or "Python"
stringLength = len(sampleString2)
newString = ""
if stringLength >= 2:
    firstLetters = sampleString2[0:2]
    lastLetters = sampleString2[-2:]
    newString = firstLetters + lastLetters
else:
    newString = "Empty String"
print(newString)

"""
3) Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first char itself.
"""
sampleString3 = str(input("Enter a string:")) or "restart"
firstLetter = sampleString3[0]
print(firstLetter+sampleString3[1:].replace(firstLetter, "$",))

"""
4) Python program to get a single string from two given strings, separated
by a space and swap the first two characters of each string.
"""
inputString1 = str(input("Enter a string:")) or 'abc'
inputString2 = str(input("Enter a string:")) or 'xyz'
outputString1 = inputString2[:2]+inputString1[2:]
outputString2 = inputString1[:2]+inputString2[2:]
print(outputString1+" "+outputString2)

"""
5) Python program to add 'ing' at the end of a given string (length should
be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
string length of the given string is less than 3, leave it unchanged.
"""
sampleString4 = str(input("Enter a string:")) or "string"
sampleLength = len(sampleString4)
if sampleLength >= 3:
    if sampleString4[-3:]=='ing':
        print(sampleString4+"ly")
    else:
        print(sampleString4+"ing")
else:
    print(sampleString4)

