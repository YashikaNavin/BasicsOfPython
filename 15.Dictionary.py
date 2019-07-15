# Dictionary
# It is unordered, changeable and indexed. It consists of key:value pair.

# Create a dictionary
a={1:'Hey', 2:'Hello', 3:'Hi'}
print(a)
print(a.keys())
print(a.values())

# Access the item
print(a[2])
print(a.get(3))   # get() can also be used to access the item from the dictionary

# Change the value
a[1]="Okay"
print(a)

# Access all items of the dictionary
for x in a:
    print(x)   # this will print all the keys present in the dictionary
    print(a[x]) # this wil print all the values of respective keys

for x in a.values():
    print(x)    # this will print all the values in the dictionary

for x,y in a.items():
    print(x,y)    # print all the keys and their resprctive values

# Check if the key exist
if 1 in a:
    print(True)

if 4  in a:
    print("Nothing")

# Length of dictionary
print(len(a))

# Add new item
a['Hey']=3
print(a)

# Remove item
a.popitem()
print(a)
a.pop(1)
print(a)

# Copy dictionary
b=a.copy()
print(b)
