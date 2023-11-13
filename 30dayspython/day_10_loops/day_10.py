#  Exercises: Day 10
# Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.
print('While loop')
i = 0
while i <= 10:
    print(i, end=" ")
    i+= 1
print()
# Iterate 10 to 0 using for loop, do the same using while loop.
print('For loop')
for i in range(0, 11):
    print(i, end=' ')

print()
# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
print('Triangle')
for i in range(7):
    for j in range(i+1):
        print('#', end=' ')
    print()
# Use nested loops to create the following:

# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
print('Rectangle')
for i in range(7):
    for j in range(7):
        print('#', end='')
    print()
# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
print('Multiply')
for i in range(11):
    print('{} X {} = {}'.format(i,i,i**2))
# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
for i in ['Python', 'Numpy','Pandas','Django', 'Flask']:
    print(i)
# Use for loop to iterate from 0 to 100 and print only even numbers
print('Even numbers')
for i in range(101):
    if i % 2 ==0:
        print(i, end=' ')
print()
# Use for loop to iterate from 0 to 100 and print only odd numbers
print('Odd numbers')
for i in range(101):
    if i % 2 != 0:
        print(i, end=' ')
print()

## Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
sum=0
for i in range(101):
    sum += i
    print(sum, end=' ')
print('\nThe sum of all numbers is', sum)
# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
sum_odd = 0
sum_even = 0
for i in range(101):
    if i % 2 == 0:
        sum_even += i
    if i % 2 != 0:
        sum_odd += i
print('The sum of even numbers', sum_even)
print('The sum of odd numbers is', sum_odd)

## Exercises: Level 3
# Go to the data folder and use the countries.py file. 
# Loop through the countries and extract all the countries containing the word land.
with open('./countries.py') as f:
    lines = f.read().splitlines()
    for i in lines:
        if 'land' in i:
            print(i)
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit = ['banana', 'orange', 'mango', 'lemon']
for i in reversed(fruit):
    print(i)

print('While fruit')
i=len(fruit) -1
print(i)
while i >= 0:
    print(fruit[i])
    i-=1

# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world
with open('./countries-data.py') as f:
    arr = []
    lines = f.read().splitlines()
    for i in lines:
        print(i)
        
    # for i in lines:
    #     print(i)
    #     arr.append(i["languages"])
    #     arr.sort()
    # print(arr)