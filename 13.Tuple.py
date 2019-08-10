# Tuple
# It is immutable(non-changeable). We cannot add, remove or change an item in tuple.

# Creating a tuple:
games=('Badminton','Cricket','Football')
print(games)
data1=(1,2,3,4)
data2=('x','y','z')
data3=(10,20,'Aman',34.5)
data4="a",10,16.5  # putting paranthesis is optional for creating tuple as python by default consider it as tuple



# Accessing tuple items:
print(games[1])
print(games[-1])
print(data1[0])
print(data1[0:2])
print(data2[-3:-1])
print(data1[0:])
print(data2[:2])
print(data3[-4:-1])
print(data4[0:])



# To get all the items of tuple
for x in games:
    print(x)
    print(id(x))  # Tuple doesn't allocate continuous memory to it's items



# Length of tuple:
print(len(games))



# count() return the number of times the given value occurs in tuple:
print(games.count('Badminton'))



# Indexing and slicing:
# When we access single value is called indexing and when we access more than one value at a time is called slicing.
a=(10,20.5,'a','Raj',30)
print(a)
print(a[3])  # example of indexing
print(a[-2])
print(a[1:3]) # example of slicing
print(a[-5:-1])
print(a[:5])
print(a[:])
print(a[0:5:2]) # this will print the item at 0 then the item at 0+2=2, then the item at 2+2=4
print(a[-1:-6]) # this will print () since the cursor never jumps backward



# Tuples can also be nested:
data1='a','Bipin',2.5
data2=data1,(10,20,30)
print(data1)
print(data2) # this is a nested tuple
print(data2[0][1])
print(data2[1][1])
print(data2[[0][0]:]) # this will print the whole data2 tuple
#print(data2[[0][1]:[1][2]]) # this will give an error



# Tuple operation:
'''Adding Tuple:- Tuple can be added by using the concatenation operatot(+) to join two tuples'''
data1=(1,2,3,4)
data2=('x','y','z')
data3=data1+data2
print(data1)
print(data2)
print(data3)

'''Replicating Tuple:- '''
data4=data3
print(data4)

'''Tuple Slicing:- A subpart of a tiple can be retrieved on the basis of index . This subpart is known as tuple alice.'''
data1=(1,2,3,4,5,6)
print(data1[0:2])
print(data1[4])
print(data1[:-1])
print(data1[-5:])
print(data1)

'''Updating elements in a Tuple:- '''
data=(10,20,30,40)
#data[0]=100 # since tuple is immutable or non-changeable you can't the change the items in a tuple
print(data)



# Creating a new Tuple from existing:
data1=(10,20,30)
data2=(40,50,60)
data3=data1+data2
print(data3)



# Deleting elements from tuple:
data=(10,20,'Deepak',30.5,'a')
print(data)
#del data[0]    # this is not possible to delete an element from the tuple as tuple is immutable 
del data
#print(data)    # this will give an error since now the tuple named data does not exist



# Functions of Tuples:
#min(tuple):- returns minimum value from tuple
data=(10,20,30.5,40.5)
print(min(data))
#max(tuple):- returns maximum value from tuple
print(max(data))
#len(tuple):- returns length of the tuple
print(len(data))
