# String

# Assign string to a variable
a="Hello" #a='Hello'
print(a)

# Multi line string can be given using '''(triple quotes)
b='''Hey!!
Yashika, this side.
All the best wishes to you:)'''
print(b)

# String as array
c='Happy Day'
print(c)
print(c[2])
print(c[5])
print(c[-3])

# String slicing or substring
print(c[2:7])
print(c[-5:-1])

# strip() is a function to remove any whitespace from front and end
d="   Hello    "
print(d)
print(d.strip())

# len() to get the length of string
print(len(a))
print(len(b))
print(len(c))
print(len(d))

# lower() to convert string in lowercase
e="ABCDE"
print(e)
print(e.lower())

# upper() to convert string in uppercase
f="fhgkjhlh"
print(f)
print(f.upper())

# replace() is used to replace a character in a string
g="CAT"
print(g)
print(g.replace('C', 'B'))

# split() split the string into substring if it finds an instance
h="Cat,Bat,Rat,Hat,Mat"
print(h)
print(h.split(','))

# format()
i="This is a {} place which is {} km far from {}."
x='beautiful'
y=5
z="Delhi"
print(i.format(x,y,z))
