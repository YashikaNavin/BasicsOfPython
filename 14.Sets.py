# Sets
# It is unordered and immutable i.e. the item in the set can't be changed but a new item can be added or an item can be removed from the set.

# Create a set
set1={12, 31, 37, 37892, 938.990}
print(set1)

# add()
set1.add("Hello")
print(set1)

# remove()
set1.remove("Hello")
print(set1)

# pop() removes any item
set1.pop()
print(set1)

# len()
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
