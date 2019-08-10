# Sets
# It is unordered and immutable i.e. the item in the set can't be changed but a new item can be added or an item can be removed from the set.
# It is created using {} and in set repetition is not allowed.


# Create a set
set1={12, 31, 37, 37892, 938.990}
print(set1)
print(type(set1))
set2=set({23,46,79,90,24})  # another way of creating set by using set() method
print(set2)



# Set Data Type Manipulation:
# add() is used to add an element in set 
set1.add("Hello")
print(set1)

# remove() is used to delete an element from set
set1.remove("Hello")
print(set1)

# pop() removes any item
set1.pop()
print(set1)

# len() tells the length of the set
print(len(set1))

# union()
set2={12, 5657, "Hi"}
print(set2)
x=set1.union(set2)
print(x)

# intersection()
print(set1.intersection(set2))

# difference()
print(set1.difference(set2))
print(set2.difference(set1))

# clear() to empty the set but not delete it
set1.clear()
print(set1)

# frozenset() function is used to make a set immutable
courses=frozenset(['Java','PHP','Python'])
print(courses)
#courses.add('C++')     # it gives error since now the set has become immutable
#courses.remove('PHP')  # it gives error since now the set has become immutable

# To copy elements from one set to another empty set
courses={'Java','PHP','Python'}
a=set(courses)
print(a)
