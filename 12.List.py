# List

# Create a list
mylist=['Apple', 'Banana', 'Coconut', 'Dates']
print(mylist)
number=[1, 2.3, -57, 'Hello']
print(number)

# Access item from list
print(mylist[2])
print(mylist[-1])

# Access all items of list using loop
for x in mylist:
 print(x)
 print(id(x)) # this line tells that list doesn't occupies continuous memory

# Change the item
mylist[2]='Carrot'
print(mylist)

# Length of list
print(len(mylist))

# To check if that item is in the list or not
if 1 in number:
    print("Yes 1 is in the list number.")

if 2 in number:
    print("True")

# To add item in list there are two methods append() and insert()
mylist.append('Orange')
print(mylist)
number.insert(1, 'Inserted')
print(number)
mylist.append(number)   # here number is append to mylist as an item 
print(mylist)
print(mylist[5])

# To remove an item
mylist.remove('Dates')
print(mylist)
mylist.pop(0)
print(mylist)
mylist.pop()  # pop() removes the item from the end of the list if you don't provide an index
print(mylist)

# del keyword is used to delete the indexed item
del mylist[2]
print(mylist)

# clear() is used to empty the list
mylist.clear()
print(mylist)

# To copy a list in another
newlist=number.copy() # 1st way to copy a list
print(newlist)
newlist1=list(number) # 2nd way to copy a list
print(newlist1)

