"""
11) Python program to create a lambda function that adds 15 to a given
number passed in as an argument, also create a lambda function that multiplies
argument x with argument y and print the result.
"""
fifteen = lambda num: num + 15
multiplyTwo = lambda num1, num2: num1 * num2

print(fifteen(15))
print(multiplyTwo(15, 15))

"""
12) Python program to create a function that takes one argument, and
that argument will be multiplied with an unknown given number.
"""


def unknownMultiply(num):
    return lambda random: random * num


result = unknownMultiply(2)
print("Calling the function with random number:", result(12))

"""
13) Python program to sort a list of tuples using Lambda.
"""
tupleList = [(0, 'c'), (1, 'a'), (2, "b")]
print("Tuple before sorting:", tupleList)
tupleList.sort(key=lambda x: x[1])
print("Tuple after sorting:", tupleList)

"""
14) Python program to sort a list of dictionaries using Lambda
"""
sampleDict = [{'number': '0', 'spelling': 'zero'}, {'number': '2', 'spelling': 'two'},
              {'number': '1', 'spelling': 'one'}]
print("Existing list:", sampleDict)
sampleDict.sort(key=lambda x: x['spelling'])
print("After sorting:", sampleDict)

"""
15) Python program to filter a list of integers using Lambda
"""
sampleList = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
print("Original List:", sampleList)
positiveList = list(filter(lambda x: x > 0, sampleList))
negativeList = list(filter(lambda x: x < 0, sampleList))
neutralList = list(filter(lambda x: x == 0, sampleList))
print("Positive List", positiveList)
print("Negative List", negativeList)
print("Neutral List", neutralList)

