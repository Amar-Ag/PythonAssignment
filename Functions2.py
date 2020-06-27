def checkInRange(number):
    """ 6) Python function to check whether a number is in a given range. """
    if number in range(1, 101):
        print("%d is in range 1-100." % number)
    else:
        print("%d is not in range 1-100." % number)


checkInRange(20)


def countUpperLower(demoString):
    """7) Python function that accepts a string and calculate the number of
        upper case letters and lower case letters"""
    upperCount = 0
    lowerCount = 0
    for i in demoString:
        if i.isupper():
            upperCount += 1
        else:
            lowerCount += 1
    return upperCount, lowerCount


demoString = str(input("Enter a string:"))
upper, lower = countUpperLower(demoString)
print("No. of Upper case characters:", upper, "\nNo. of Lower case characters:", lower)


def uniqueList(repeatList):
    """ 8) Python function that takes a list and returns a new list with unique
    elements of the first list."""
    repeatList = list(set(repeatList))
    return repeatList


print(uniqueList([1, 1, 1, 12, 2, 2, 22, 2, 3, 3, 3]))


def checkPrime(number):
    """ 9) Python function that takes a number as a parameter and check the
        number is prime or not."""
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number")
                break
        else:
            print(number, "is a prime number")
    else:
        print(number, "is not a prime number")


inputNumber = int(input("Enter any number:"))
checkPrime(inputNumber)

"""
10) Python program to print the even numbers from a given list.
"""
sampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newList = []
for i in sampleList:
    if i % 2 == 0:
        newList.append(i)
print("List with only even numbers:", newList)
