#There is a input() use to take input from the user

name=input("What's your name?\n")
age=input("What is your age?\n")
print("Your name is " + name + " and you are " + age + " years old")


#The input() takes the input as string so we need to do type casting to get the input in other data type

a=int(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
c=a+b
print("The value of c after addition will be ", c)
