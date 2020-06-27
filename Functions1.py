def addThreeNos(var1, var2, var3):
    """1) Python function to find the Max of three numbers."""
    return var1 + var2 + var3


print(addThreeNos(1, 2, 3))


def listSum(demoList):
    """ 2) Python function to sum all the numbers in a list."""
    return sum(demoList)


print(listSum([8, 2, 3, 0, 7]))


def listProduct(demoList):
    """ 3) Python function to multiply all the numbers in a list."""
    product = 1
    for i in demoList:
        product *= i
    return product


print(listProduct([8, 2, 3, -1, 7]))


def reverseString(demoString):
    """ 4) Python program to reverse a string."""
    revString = demoString[::-1]
    return revString


demoString = str(input("Enter a string to be reversed:")) or "checkString"
print(reverseString(demoString))


def returnFactorial(number):
    """ 5) Python function to calculate the factorial of a number (a non-negative
        integer). The function accepts the number as an argument."""
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact


inputNumber = int(input("Enter a number to calculate factorial for:"))
print("Factorial of", inputNumber, "is:", returnFactorial(inputNumber))
