#### Exercises: Day 7
# # sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#$ Exercises: Level 1
# Find the length of the set it_companies
print(len(it_companies))
# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
# Insert multiple IT companies at once to the set it_companies
it_companies.update({'Samsung', 'Yahoo'})
print(it_companies)
# Remove one of the companies from the set it_companies
del it_companies
# What is the difference between remove and discard
''' We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set. 
However, discard() method doesn't raise any errors.'''

## Exercises: Level 2
# Join A and B
print(A)
print(B)
C= A.union(B)
print(C)
# Find A intersection B
print(A.intersection(B))
# Is A subset of B
print(A.issubset(B))
# Are A and B disjoint sets
print(A.isdisjoint(B))
# Join A with B and B with A
print(A.union(B))
print(B.union(A))
# What is the symmetric difference between A and B
print(A.symmetric_difference(B))
# Delete the sets completely
del A
del B


## Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_st = set(age)
print(age_st)
# Explain the difference between the following data types: string, list, tuple and set
'''
Text is a string data type. 
Any data type written as text is a string. Any data under single, double or triple quote are strings.
''' 
'''
A list is collection of different data types which is ordered and modifiable(mutable). 
A list can be empty or it may have different data type items.
'''
'''
A tuple is a collection of different data types which is ordered and unchangeable (immutable). 
Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. 
We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable).
'''
'''
Set is a collection of items. Set is a collection of unordered and un-indexed distinct elements.
In Python set is used to store unique items, and it is possible to find the union, intersection, 
difference, symmetric difference, subset, super set and disjoint set among sets.
'''
# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.


# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
me = 'I am a teacher and I love to inspire and teach people.'.split()
print(me)
me_st = set(me)
print(me_st)
print(len(me_st))