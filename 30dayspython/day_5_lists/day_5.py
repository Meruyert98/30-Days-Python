###  Exercises: Day 5
# Exercises: Level 1

# Declare an empty list
empty_list = list()
empty_list = []
print(empty_list)
# Declare a list with more than 5 items
fruit = ['banana', 'apple','watermelon', 'melon', 'mango']
print(fruit)
# Find the length of your list
print(len(fruit))
# Get the first item, the middle item and the last item of the list
print(fruit[0]) #first item
middle= (len(fruit)-1)//2 
print(fruit[middle]) #middle item
print(fruit[-1]) #last item
print(fruit[len(fruit)-1]) #last item
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Meruyert', 'age', '1.62', 'single', 'Kazakhstan']
print(mixed_data_types)
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# Print the list using print()
print(it_companies)
# Print the number of companies in the list
print(len(it_companies))
# Print the first, middle and last company
print(it_companies[0])
print(it_companies[(len(it_companies)-1)//2])
print(it_companies[-1])
# Print the list after modifying one of the companies
it_companies[5] = 'Samsung'
print(it_companies)
# Add an IT company to it_companies
it_companies.append('Oracle')
print(it_companies)
# Insert an IT company in the middle of the companies list
it_companies.insert((len(it_companies)-1)//2, 'Dell')
print(it_companies)
# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)
# Join the it_companies with a string '#;  '
print('#; '.join(it_companies))
# Check if a certain company exists in the it_companies list.
print('IBM' in it_companies)
# Sort the list using sort() method
it_companies.sort()
print(it_companies)
# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
# Slice out the first 3 companies from the list
print(it_companies[3:])
# Slice out the last 3 companies from the list
print(it_companies[:-3])
# Slice out the middle IT company or companies from the list
print(it_companies[(len(it_companies)-1)//2])
# Remove the first IT company from the list
del it_companies[0]
print(it_companies)
# Remove the middle IT company or companies from the list
del it_companies[(len(it_companies)-1)//2]
print(it_companies)
# Remove the last IT company from the list
it_companies.pop()
print(it_companies)
# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
# del it_companies
# print(it_companies)

# Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)


### Exercises: Level 2

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)
# Sort the list and find the min and max age
ages.sort()
print(ages)
print('Max age', ages[-1])
print('Min age', ages[0])
# Add the min age and the max age again to the list
ages.insert(0, 16)
ages.append(30)
print(ages)
# Find the median age (one middle item or two middle items divided by two)
middle = (len(ages)-1)//2
if middle%2==0:
    print(ages[middle])
else: print(ages[middle], ages[middle+1])
# Find the average age (sum of all items divided by their number )
sumn = 0
for i in ages:
    sumn += i
average = sumn/len(ages)
print('Average age is {:.2f}'.format(average))
# Find the range of the ages (max minus min)
print('Range of the list', ages[-1]-ages[0])
# Compare the value of (min - average) and (max - average), use abs() method
print(abs(ages[0]-average) < abs(ages[-1]-average))
# Find the middle country(ies) in the countries list
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
country = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle = (len(country)+1)//2
first_half = country[:middle]
second_half = country[middle:]
print(first_half)
print(second_half)
