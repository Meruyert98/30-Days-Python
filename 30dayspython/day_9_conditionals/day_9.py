###  Exercises: Day 9

## Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
age = int(input('Enter your age: '))
if age > 18:
    print('You are old enough to learn to drive.')
else:
    print('You need {} more years to learn to drive.'.format(18-age))
# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.
my_age = 25
your_age = int(input('Enter your age: '))
diff = your_age - my_age 
if your_age < my_age:
    print('You are smaller than me')
elif your_age == my_age:
    print('You are my age')
elif diff == 1:
    print('You are 1 year older than me')
else:
    print('You are {} years older than me'.format(diff))
# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
a = int(input("Enter a: "))
b = int(input("Enter b: "))
if a > b:
    print('{} is greater than {}'.format(a,b))
elif a < b:
    print('{} is less than {}'.format(a,b))
else:
    print('{} is equal to {}'.format(a,b))

# ### Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
score = int(input("Enter your score: "))
if score >= 90:
    print('A')
elif score >= 70 and score < 90:
    print('B')
elif score >= 60 and score < 70:
    print('C')
elif score >= 50 and score < 60:
    print('D')
else:
    print('F')
# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input('Enter month: ')
month.title()
if month in ['September', 'October','November']:
    print('Autumn')
elif month in ['December', 'January', 'February']:
    print('Winter')
elif month in ['March', 'April','May']:
    print('Spring')
elif month in ['June', 'July', 'August']:
    print('Summer')
else:
    print('There is no such month')
# The following list contains some fruits:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter fruit: ')
if fruit in fruits:
    print('That fruit already exist in the list')
else: 
    fruits.append(fruit)
    print(fruits)
# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
print(person)
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person.keys():
    middle = (len(person['skills']) - 1)//2
    print(person.get('skills')[middle])
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person.keys():
    if 'Python' in person.get('skills'):
        print('Person has Python as a skill')

#  * If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!
skills = person['skills']
if ['Javascript', 'React'] in skills:
    print('He is a front end developer')
if ['Node', 'Python', 'MongoDB'] in skills:
    print('He is a backend developer')
if ['React', 'Node','MongoDB'] in skills:
    print('He is a fullstack developer')
if ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'] in skills:
    print('Super Coder')
else: 
    print('unknown title')
#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.
