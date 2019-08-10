# Dictionary
# It is unordered(in case of python version 3.5 or less than that)/ordered(in case of python version 3.6 and above that), changeable and indexed. It consists of key:value pair.
'''Dictionary is an ordered set of key and value pair.
It is an container that contains data, enclosed within curly braces.
The pair i.e., key and value is known as item.
The key passed in the item must be unique.
The key and the value is separated by a colon(:). This pair is known as item.
Items areseparated from eachother by a comma(,).
Different items are enclosed within a curly brace and this forms Dictionary.
Dictionary is mutable i.e., value can be updated.
Dictionary is known as Associative array since the key works as Index and they are decided by the user.'''

# Create a dictionary
a={1:'Hey', 2:'Hello', 3:'Hi'}
print(a)
print(a.keys())
print(a.values())
data={100:'Ravi', 101:'Vijay', 102:'Rahul'}
print(data)
plant={} # you can create an empty dictionary and then put value in that dictionary
plant[1]='Ravi'
plant[2]='Manoj'
plant['name']='Hari'
plant[4]='Om'
print(plant[2])
print(plant['name'])
print(plant[1])
print(plant)

# Access the item
print(a[2])
print(a.get(3))   # get() can also be used to access the item from the dictionary

# Change the value
a[1]="Okay"
print(a)
data1={'Id':100, 'Name':'Suresh', 'Profession':'Developer'}
data2={'Id':101, 'Name':'Ramesh', 'Profession':'Trainer'}
data1['Profession']='Manager'
data2['Salary']=20000 # since this key is not present in dictionary so it will be automatically added in that dictionary with its value 
data1['Salary']=15000 # since this key is not present in dictionary so it will be automatically added in that dictionary with its value 
print(data1)
print(data2)

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



# Dictionary Methods:
# Add new item
a['Hey']=3
print(a)

# Remove item
a.popitem()
print(a)
a.pop(1)
print(a)

# Copy dictionary - copy() returns an ordered copy of the data
b=a.copy()
print(b)

# del keyword is used to delete either the element or the whole dictionary
data={100:'Ram', 101:'Suraj', 102:'Alok'}
del data[102]
print(data)
del data
#print(data) # will show an error since dictionary is deleted

# keys() returns all the keys element of a dictionary
data1={100:'Ram', 101:'Suraj', 102:'Alok'}
print(data1.keys())

# values() returns all the values element of a dictionary
data1={100:'Ram', 101:'Suraj', 102:'Alok'}
print(data1.values())

# items() returns all the items(key-value pair) of a dictionary
data1={100:'Ram', 101:'Suraj', 102:'Alok'}
print(data1.items())

# clear() is used to remove all items of a dictionary
data1={100:'Ram', 101:'Suraj', 102:'Alok'}
print(data1)
data1.clear() # this will only clear the items in the dictionary but not delete the dictionary
print(data1)

# update(dictionary 2) is used to add items of dictionary 2 to first dictionary
data1={100:'Ram', 101:'Suraj', 102:'Alok'}
data2={103:'Sam'}
data1.update(data2)
print(data1)
print(data2)

#fromkeys(sequence)/fromkeys(seq,value) is used to create a new dictionary from the sequence
sequence=('Id','Number','Email')
data={}
data1={}
data=data.fromkeys(sequence)
print(data)
data1=data1.fromkeys(sequence,100)
print(data1)

#get(key) returns the value of the given key. If key is not present it will return none.
data={'Id':100,'Name':'Akash','Age':23}
print(data.get('Age'))
print(data.get('Email'))



# Nested Dictionary:
# Create a nested dictionary
employees={1:{'name':'Aman','age':'27','gender':'Male'},
           2:{'name':'Raj','age':'22','gender':'Male'},
           3:{'name':'Deepak','age':'30','gender':'Male'}}
print(employees)
print(employees[1]['name'])
print(employees[1]['age'])
print(employees[1]['gender'])

# Change or add elements in a nested dictionary
employees[4]={}
employees[4]['name']='Saroj'
employees[4]['age']='24'
employees[4]['gender']='Female'
print(employees[4])
print(employees)

# Delete elements from a nested dictionary
del employees[3]['age']
print(employees[3])

# Delete dictionary from a nested dictionary
del employees[3], employees[4]
print(employees)
