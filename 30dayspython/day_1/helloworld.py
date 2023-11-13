#### Exercises - Day 1
### Exercise: Level 1

## Check the python version you are using
# python --version

## Open the python interactive shell and do the following operations. The operands are 3 and 4.
# addition(+)
print(3+4)
# subtraction(-)
print(3-4)
# multiplication(*)
print(3*4)
# modulus(%)
print(3%4)
# division(/)
print(3/4)
# exponential(**)
print(3**4)
# floor division operator(//)
print(3//4)
# Write strings on the python interactive shell. The strings are the following:
# Your name
print('Meruyert')
# Your family name
print('Slamova')
# Your country
print('Kazakhstan')
# I am enjoying 30 days of python
print('I am enjoying 30 days of python')
# Check the data types of the following data:
# 10
print(type(10))
# 9.8
print(type(9.8))
# 3.14
print(type(3.14))
# 4 - 4j
print(4-4j)
# ['Asabeneh', 'Python', 'Finland']
print(['Asabeneh', 'Python', 'Finland'])
# Your name
print('Meruyert')
# Your family name
print('Slamova')
# Your country
print('Kazakhstan')

## Exercise: Level 2
# Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it.
# Exercise: Level 3
# Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
# Checking data types

# Integer: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...
print(type(10))          # Int
# Float: Decimal number Example ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
print(type(3.14))        # Float
# Complex Example 1 + j, 2 + 4j
print(type(1 + 3j))      # Complex number
# A collection of one or more characters under a single or double quote. If a string is more than one sentence then we use a triple quote.
print(type('Asabeneh'))  # String
# A boolean data type is either a True or False value. T and F should be always uppercase.
print(type(True))  # String
# Python list is an ordered collection which allows to store different data type items. A list is similar to an array in JavaScript.
print(type([1, 2, 3]))   # List
# A Python dictionary object is an unordered collection of data in a key value pair format.
print(type({'name':'Asabeneh'})) # Dictionary
# A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items.
print(type({9.8, 3.14, 2.7}))    # Set
# A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.
print(type((9.8, 3.14, 2.7)))    # Tuple

# Find an Euclidian distance between (2, 3) and (10, 8)
print((2-3)**2+(10-8)**2)