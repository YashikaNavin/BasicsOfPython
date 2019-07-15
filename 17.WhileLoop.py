# While
i=1
while i<6:
    print(i)
    i+=1

# Using break to stop the loop in between
i=1
while i<6:
    print(i)
    if i==3:
        break
    else:
        i+=1

# continue statement
i=1
while i<6:
    i+=1
    if i==3:
        continue
    print(i)
