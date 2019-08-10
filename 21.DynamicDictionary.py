# Create dynamic dictionary:

my_dict=dict()

n=int(input("Enter number of elements:"))

for i in range(0,n):
    user_input=input("Enter key and value separated by commas (,):")
    key,value=user_input.split(',')
    my_dict[key]=value

print(my_dict)
