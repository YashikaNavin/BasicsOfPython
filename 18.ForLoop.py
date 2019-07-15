# For loop in python just work as an iteration method unlike other programming languages
for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print(x)

# break statement
for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print(x)
    if x=='D':
        break

# continue statement
for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if x=='D':
        continue
    print(x)

# range()
for x in range(6): # the loop starts from 0 and ends to one less than the given number in the range()
    print(x)

for x in range(2,6):  # the loop starts from 2 
    print(x)

for x in range(1,6,2): # the third argument in range() tells that by how much the loop will incremented
    print(x)


