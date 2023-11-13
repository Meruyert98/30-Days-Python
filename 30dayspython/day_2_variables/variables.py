### Exercises - Day 2
## Exercises: Level 1

# Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
# Write a python comment saying 'Day 2: 30 Days of python programming'
# Day 2: 30 Days of python programming

# Declare a first name variable and assign a value to it
first_name = 'Meruyert'
print('First name:', first_name)
# Declare a last name variable and assign a value to it
last_name = 'Slamova'
print('Last name:', last_name)
# Declare a full name variable and assign a value to it
full_name = 'Meruyert Slamova'
print('Full name:', full_name)
# Declare a country variable and assign a value to it
country = 'Kazakhstan'
print('Country:', country)
# Declare a city variable and assign a value to it
city = 'Almaty'
print('City:', city)
# Declare an age variable and assign a value to it
age = 25
print('Age:', age)
# Declare a year variable and assign a value to it
year = 2023
print('Year:', year)
# Declare a variable is_married and assign a value to it
is_married = False
print('Is married:', is_married)
# Declare a variable is_true and assign a value to it
is_true = True
# Declare a variable is_light_on and assign a value to it
is_light_on = True
# Declare multiple variable on one line
full_name, age, is_marred = 'Slamova Gaukhar', 25, False
print(full_name, age, is_married)
# Exercises: Level 2
# Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(age))
print(type(is_married))
print(first_name, last_name, country, age, is_married)
# Using the len() built-in function, find the length of your first name
print('Length first name:', len(first_name))
# Compare the length of your first name and your last name
print('Len first_name', len(first_name), 'and len last name', len(last_name))
# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print('Addition:',total)
# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print('Subtraction:',diff)
# Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print('Multiply:', product)
# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print('Divide:', division)
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print('Modulus:', remainder)
# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print('Exponenta:', exp)
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one//num_two
print('Floor division:', floor_division)
# The radius of a circle is 30 meters.
radius = 30
print('Radius of a circle:', radius)
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = 3.14 * (radius**2)
print('Area of a circle:', area_of_circle)
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2*3.14*radius
print('Circumference of a circle:', circum_of_circle)
# Take radius as user input and calculate the area.
u_radius = int(input('Enter radius: '))
print('Area of a user circle:', 3.14 * (u_radius**2))
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input('Input your first name: ')
last_name = input('Input your last name: ')
country = input('Input your country: ')
age = input('Input your age: ')
print('My name is '+first_name+' '+last_name+'. '+'I am '+age)
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
