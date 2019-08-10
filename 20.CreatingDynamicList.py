# Get a list as input from user or create a dynamic list:
li=[] # create empty list

n=int(input("Enter number of elements:")) # number of elements as input

for i in range(0,n):
    ele=int(input())
    li.append(ele) # adding the element

print(li)



# Create a list of list:
li=[]
n=int(input("Enter number of elements:"))

for i in range(0,n):
    ele=[input(), int(input())]
    li.append(ele)

print(li)

