#type() is a pre-defined function to know the type of a variable

a=56
b=78.90
c=True
d="Friday"
print(a, "belongs to ", type(a))
print(b, "belongs to ", type(b))
print(c, "belongs to ", type(c))
print(d, "belongs to ", type(d))


#id() is a pre-defined function to know the address of a variable

print("Id of a = ", id(a))
print("Id of b = ", id(b))
print("Id of c = ", id(c))
print("Id of b = ", id(d))


#If we assign same value to all variables then their id will be same

e=f=0
print("Id of e = ", id(e))
print("Id of f = ", id(f))

g=0
h=0
print("Id of g = ", id(g))
print("Id of h = ", id(h))
