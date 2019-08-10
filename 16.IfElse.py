# Conditional Statement in Python:
'''Conditional statements are used to perform different actions based on different conditions.
Generally in python, conditional statements are of different types:
1. if statement
2. if..else statement
3. Nested if..else statement
4. if..elif..else statement
5. Jumping statement [break, continue, pass, return]'''


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
#This works like a switch statement since python doesn't support 'switch' as in C or Java. 
'''Syntax:-
if(condition 1):
    statement 1
elif(condition 2):
    statement 2
elif(codition 3):
    statement 3
elif(condition 4): # Number of elif conditions can be according to our need in program
    statement 4
else:
    statement 5'''
if a>b:
    print("a")
elif a==b:
    print("a and b")
else:
    print("Above two conditions are wrong.")


# Short hand if and if else
if a<b: print("a")
print("a") if a>b else print("b")


# Nested if else statement
'''Syntax:-
if(condition 1):
    if(condition 2):
        statement 1
    else:
        statement 2
else:
    if(condition 3):
        statement 3
    else:
        statement 4'''
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
if(a>b):
    if(a>c):
        print("a is greater")
    else:
        print("c is greater")
else:
    if(b>c):
        print("b is greater")
    else:
        print("c is greater")
        
