#### Exercises: Day 6

# Exercises: Level 1
# Create an empty tuple
empty_tuple = ()
empty_tuple = tuple()
print(empty_tuple)
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Aikerim', 'Akerke','Gaukhar')
brothers = ('Almas', 'Daulet')
print(sisters)
print(brothers)
# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)
# How many siblings do you have?
print(len(siblings))
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Iliyas', 'Rano')
print(family_members)


### Exercises: Level 2
# Unpack siblings and parents from family_members
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'apple', 'mango')
animal_products = ('beef', 'horse meat', 'chicken', 'ham')
food_stuff_tp = fruits + animal_products
print(food_stuff_tp)
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_tp[(len(food_stuff_tp)-1)//2])
# Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[3:-3])
# Delete the food_staff_tp tuple completely
del food_stuff_tp
# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)