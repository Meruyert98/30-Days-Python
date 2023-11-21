# Exercises: Day 11
# Exercises: Level 1

def fake_bin(x):
    arr = list(x)
    l = ''
    for i in arr:
        if int(i) > 5:
            l += '1'
        else:
            l += '0'
    return l
    
print(fake_bin('45385593107843568'))

# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a,b):
    print(a+b)

add_two_numbers(4,5)

# Area of a circle is calculated as follows: area = π x r x r. 
# Write a function that calculates area_of_circle.
def area_of_circle(r):
    PI = 3.14
    area = PI * r**2
    return area

print(area_of_circle(3))

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
#  Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(n):
    total = 0
    for i in range(n+1):
        total += i
    print(total)

add_all_nums(5)

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(n):
    F = (n*(9/5))+32
    print(F)

convert_celsius_to_fahrenheit(60)

# Write a function called check-season, it takes a month parameter 
# and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
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

check_season('June')
# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope():
    pass

# Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn():
    pass

# Declare a function named print_list. 
# It takes a list as a parameter and it prints out each element of the list.
def print_list(l):
    for i in l:
        print(i)

print_list(['December', 'January', 'February'])

# Declare a function named reverse_list. 
# It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(l):
    i= len(l)-1
    reverse = []
    while i >= 0:
        reverse.append(l[i])
        i -= 1
    return reverse

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

# Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(l):
    cap = []
    for i in l:
        cap.append(i.capitalize())
    return cap

print(capitalize_list_items(['hello','hi']))

# Declare a function named add_item. It takes a list and an item parameters. 
# It returns a list with the item added at the end.
def add_item(l, i):
    l.append(i)
    return l

print(add_item(["A", "B", "C"],"D"))
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      ##[2, 3, 7, 9, 5]

# Declare a function named remove_item. It takes a list and an item parameters. 
# It returns a list with the item removed from it.
def remove_item(l, i):
    l.remove(i)
    return l

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]

# Declare a function named sum_of_numbers. 
# It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n):
    total =0
    for i in range(n+1):
        total += i
    return total

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# Declare a function named sum_of_odds. 
# It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    total = 0
    for i in range(n+1):
        if i % 2 != 0:
            total += i
    return total

print(sum_of_odds(5))

# Declare a function named sum_of_even. 
# It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(n):
    total = 0
    for i in range(n+1):
        if i % 2 == 0:
            total += i
    return total

print(sum_of_even(5))

# Exercises: Level 2
# Declare a function named evens_and_odds . 
# It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(n):
    even = 0
    odd = 0
    for i in range(n+1):
        if i%2==0:
            even += 1
        else:
            odd += 1
    return 'The number of odds are {}. The number of evens are {}.'.format(odd, even)

print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.

# Call your function factorial, 
# it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return 'The factorial of number {} is {}.'.format(n,fact)

print(factorial(23))

# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(p=''):
    if len(str(p)) ==0:
        return "Empty"
    else:
        return "Not empty"

print(is_empty(5))

# Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, 
# calculate_range, calculate_variance, calculate_std (standard deviation).
import math
import statistics
def calc(data, ddof = 0):
    n = len(data)
    calculate_mean = sum(data) / n
    mean = statistics.mean(data)
    calculate_median = statistics.median(data)
    calculate_mode = statistics.mode(data)
    calculate_range = max(data) - min(data)
    calculate_variance = sum((x - calculate_mean) ** 2 for x in data) / (n - ddof)
    calculate_std = math.sqrt(calculate_variance)
    print("The mean is {}.".format(mean))
    print("The median is {}.".format(calculate_median))
    print("The mode is {}.".format(calculate_mode))
    print("The range is {}.".format(calculate_range))
    print("The variance is {}.".format(calculate_variance))
    print("The std is {}.".format(calculate_std))

calc([1, 2, 3, 3, 4])

# Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n == 1:
        print(n, 'is not a prime number.')
    elif n > 1:
        if n%2==0:
            print(n, 'is not a prime number.')
        else:
            print(n, 'is a prime number')
is_prime(5)
is_prime(6)

# Write a functions which checks if all items are unique in the list.
def unique_items(l):
    l_set = list(set(l))
    if len(l_set) == len(l):
        print('All numbers unique')
    else:
        print('Numbers are not unique')

unique_items([1,2,3,4])
unique_items([1,2,3,4,2])
# Write a function which checks if all the items of the list are of the same data type.
def same_type(l):
    res = all(isinstance(sub, type(l[0])) for sub in l[1:])
    print("Do all elements have same type : " + str(res))

same_type([5, 6, 2, 5, 7, 9, 2.12])

# Write a function which check if provided variable is a valid python variable
def check_valid_var(v):
    print('Provided variable is a valid python variable:', v.isidentifier())

check_valid_var('check')
check_valid_var('2')

# Go to the data folder and access the countries-data.py file.
from countries_data import data
def opendata(data):
    for country in data:
        print(country)
opendata(data)

# Create a function called the most_spoken_languages in the world. 
# It should return 10 or 20 most spoken languages in the world in descending order
def most_spoken(data):
    dict = {}
    for country in data:
        for lan in country['languages']:
            if lan in dict:
                dict[lan]+=1
            else:
                dict[lan]=1
    arr = list(dict.values())
    arr.sort(reverse=True)
    arr = arr[:10]
    result = []
    for i in arr:
        for key in dict:
            if i == dict[key]:
                result.append(key)
    print('10 most spoken languages')
    print(list(set(result))[:10])

most_spoken(data)
# Create a function called the most_populated_countries. 
# It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(data):
    dict = {}
    arr = []
    for country in data:
        arr.append(country["population"])
    arr.sort(reverse=True)
    arr = arr[:10]
    result = []
    for i in arr:
        for j in data:
            if i == j['population']:
                result.append(j['name'])
    print("Most populated countries")
    print(result)

most_populated_countries(data)