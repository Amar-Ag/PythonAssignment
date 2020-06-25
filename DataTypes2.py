"""
6) Python program to find the first appearance of the substring 'not' and
'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
substring with 'good'. Return the resulting string.
"""
sampleInput = str(input("Enter any string:")) or "The lyrics is not that poor!"
wordOne = "not"
wordTwo = "poor"
if wordOne in sampleInput:
    notIndex = sampleInput.index(wordOne, 1)
    if wordTwo in sampleInput:
        poorIndex = sampleInput.index(wordTwo, 1)
        if notIndex < poorIndex:
            print(sampleInput[:notIndex] + "good" + sampleInput[poorIndex + 4:])
    else:
        print("The string was not changed:", sampleInput)
else:
    print("The string was not changed:", sampleInput)

"""
7) Python function that takes a list of words and returns the length of the
longest one.
"""


def longestWord(wordList):
    largest = 0;
    for i in wordList:
        wordLength = len(i)
        if wordLength > largest:
            largest = wordLength
    return largest


sampleList = ['This', 'is', 'an', 'assignment', 'for', 'learning', 'Python']
print("Largest length in the supplied list is:", longestWord(sampleList))

"""
8) Python program to remove the n th index character from a nonempty string.
"""
sampleString = str(input("Enter a string:")) or "Python"
indexToRemove = int(input("Enter the index that you want to remove:"))
print(sampleString[:indexToRemove] + sampleString[indexToRemove + 1:])

"""
9) Python program to change a given string to a new string where the first
and last chars have been exchanged.
"""
sampleString2 = str(input("Enter a string:")) or "Python"
newString = sampleString2[-1].upper() + sampleString2[1:-1] + sampleString2[0].lower()
print(newString)

"""
10) Python program to remove the characters which have odd index
values of a given string.
"""
sampleString3 = str(input("Enter a string:")) or "Python"
evenString = ""
for i in sampleString3:
    index = sampleString3.find(i)
    if index % 2 == 0:
        evenString += i
print(evenString)
