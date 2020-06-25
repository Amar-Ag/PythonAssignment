"""
11) Python program to count the occurrences of each word in a given
sentence.
"""
sampleSentence = str(input("Enter a sentence:")) or "This is a sample Python sentence for Python assignment"
sentenceWords = sampleSentence.split(" ")
countDict = {}
print(sentenceWords)
for word in sentenceWords:
    keys = countDict.keys()
    if word in keys:
        countDict[word] += 1
    else:
        countDict[word] = 1
print(countDict)

"""
12) Python script that takes input from the user and displays that input
back in upper and lower cases.
"""
sampleInput = str(input("Enter sample input:")) or "Sample Input"
print("Upper Case:", sampleInput.upper())
print("Lower Case:", sampleInput.lower())

"""
13) Python program that accepts a comma separated sequence of words
as input and prints the unique words in sorted form (alphanumerically).
"""
sampleWords = str(input("Enter comma separated sequence of words")) or "red, white, black, red, green, black"
sampleWords = sampleWords.split(',')
sampleWords = list(
    set(sampleWords))  # Converting to set 1st to keep the unique elements and converting the set to a list
print(",".join(sorted(sampleWords)))  # Sorting the list alphanumerically and then joining each element with a comma
# output includes ' red' and 'red' as different items due to the space ahead

"""
14) Python function to create the HTML string with tags around the
word(s).
"""


def add_tags(tag, dummyText):
    return "<" + tag + ">" + dummyText + "</" + tag + ">"


dummyText = str(input("Enter text to be included in HTML tags:")) or "Python"
tag = str(input("Enter the tag you want:")) or "b"
print(add_tags(tag, dummyText))

"""
15) Python function to insert a string in the middle of a string.
"""


def insert_string_middle(firstStr, SecondStr):
    stringLength = len(firstStr)
    middleIndex = int(stringLength / 2)
    newString = firstStr[:middleIndex] + SecondStr + firstStr[middleIndex:]
    return newString


firstString = str(input("Enter first string:")) or "[[{}]]"
secondString = str(input("Enter second string:")) or "Python"
print(insert_string_middle(firstString, secondString))
