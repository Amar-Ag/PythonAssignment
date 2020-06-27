"""
16) Python program to square and cube every number in a given list of
integers using Lambda
"""
from functools import reduce

sampleList = [1, 2, 3, 4, 5]
print("Original List:", sampleList)
print("Sqaured List:", list(map(lambda x: x ** 2, sampleList)))
print("Cubed List:", list(map(lambda x: x ** 3, sampleList)))

"""
17) Python program to find if a given string starts with a given character
using Lambda.
"""
sampleString = str(input("Enter a string:")) or "String"
sampleChar = str(input("Enter character to test from:")) or "S"
checkStart = lambda string, char: True if string[0] == char else False
print(checkStart(sampleString, sampleChar))

"""
18) Python program to find if a given string starts with a given character using Lambda.
"""
sampleNumber = input("Enter any input:")
checkNumber = lambda num: num.isdigit()
checkSign = lambda num: checkNumber(num[1:]) if num[0] == "-" else checkNumber(num)
print(checkSign(sampleNumber))

"""
19) Python program to create Fibonacci series upto n using Lambda
"""
sampleNumber2 = int(input("Enter any number:"))
fibonaaciGenerator = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
                                      range(n - 2), [0, 1])
print(fibonaaciGenerator(sampleNumber2))

"""
20) Python program to find intersection of two given arrays using Lambda.
"""
electonics = ["TV", "Mobile", "Refrigerator", "Laptop"]
appleProducts = ["TV", "Mobile", "Laptop"]
print("Original arrays:")
print(electonics)
print(appleProducts)
appleElectronics = list(filter(lambda x: x in electonics, appleProducts))
print("Common items ", appleElectronics)
