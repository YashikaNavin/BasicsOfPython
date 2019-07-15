# if
a=10
b=20
if a<b:
    print("a is smaller than b")

# if else
if a>b:
    print("a is greater than b")

else:
    print("a is smaller than b")

# if elif
if a>b:
    print("a")
elif b>a:
    print("b")

# if elif else
if a>b:
    print("a")
elif a==b:
    print("a and b")
else:
    print("Above two conditions are wrong.")

# Short hand if and if else
if a<b: print("a")
print("a") if a>b else print("b")
    
