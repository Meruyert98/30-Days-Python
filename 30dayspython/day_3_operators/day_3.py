### Exercises - Day 3

## Arithmetic Operators:
# Addition(+): a + b
# Subtraction(-): a - b
# Multiplication(*): a * b
# Division(/): a / b
# Modulus(%): a % b
# Floor division(//): a // b
# Exponentiation(**): a ** b

## Logical Operators
# Unlike other programming languages python uses keywords and, or and not for logical operators. 
# Logical operators are used to combine conditional statements: AND, OR, NOT


# Declare your age as integer variable
age = 25
print('Age:', age)

# Declare your height as a float variable
height = 1.62
print('Height:', height)

# Declare a variable that store a complex number
complex = 1+4j
print('Complex number:', complex)

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100
b = int(input('Enter base: '))
h = int(input('Enter height: '))
area = 0.5 * b * h
print('The area of the triangle is', area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12
a = input('Enter side a: ')
b = input('Enter side b: ')
c = input('Enter side c: ')
p = a+b+c
print('The perimeter of the triangle is', p)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = input('Enter length of rectangle: ')
width = input('Input width of a rectangle: ')
area = length * width
perimeter = 2 * (length + width)
print('Area of the rectangle is', area)
print('Perimater of the rectangle is', perimeter)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = input('Radius of a circle: ')
pi = 3.14
area = pi * r * r
c = 2 * pi * r
print('Area of the circle is', area)
print('Circumference of the circle is', c)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Compare the slopes in tasks 8 and 9.
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python')>len('dragon'))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon.')

# There is no 'on' in both dragon and python
print('on' not in 'python' and 'on' not in 'dragon')

# Find the length of the text python and convert the value to float and convert it to string
print(float('12.3'))
print(str(12.3))

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input('Enter your number: '))
remainder = number % 2
print('Even number:', remainder is 0)
print('Even number check: ', remainder == 0)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division = 7 // 3
print(floor_division == int(2.7))

# Check if type of '10' is equal to type of 10
print(type('10') is type(10))

# Check if int('9.8') is equal to 10
print(int('9.8') is 10)

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
hour = input('Enter hour: ')
rate = input('Enter rate per hour: ')
print('Your weekly earning is', hour * rate)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.
years = input('Enter number of years you have lived: ')
second =  years * (365*24*60*60)
print('You have lived for '+second+' seconds.')

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
