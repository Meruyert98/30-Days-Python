### Exercises: Day 8

# Create an empty dictionary called dog
dog = {}
print(dog)
# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Arlan'
dog['color'] = 'white'
dog['breed'] = 'Alabai'
dog['legs'] = 4
dog['age'] = 15
print(dog)
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = { 'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Kazakhstan',
    'city':'Almaty',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
        }
print(student)
# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
print(student.get('skills'))
print(type(student.get('skills')))
# Modify the skills values by adding one or two skills
student['skills'].append('HTML')
print(student)
# Get the dictionary keys as a list
print(student.keys())
# Get the dictionary values as a list
print(student.values())
# Change the dictionary to a list of tuples using items() method
print(student.items())
# Delete one of the items in the dictionary
print(student.pop('address'))
print(student)
# Delete one of the dictionaries
del student