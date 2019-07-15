# Numbers
a=56
b=32562709545676454456373412084736272839
c=75.9
d=complex(3,7)  # complex() is a function in python to convert real number into complex number
e=9-6j
print("a=", a, "of type", type(a))
print("b=", b, "of type", type(b))
print("c=", c, "of type", type(c))
print("d=", d, "of type", type(d))
print("e=", e, "of type", type(e))


# Type Conversion
x=12324
y=6389.837409
z=57+49j # Complex number can't be changed into integer or float
print("x=", x, "of type", type(x))
print("y=", y, "of type", type(y))
print("z=", z, "of type", type(z))

m=int(y)
n=float(x) 
o=complex(y) 
print("m=", m, "of type", type(m))
print("n=", n, "of type", type(n))
print("o=", o, "of type", type(o))


# Random Number
import random
print(random.randrange(1,10))
