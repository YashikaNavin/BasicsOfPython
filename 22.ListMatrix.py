# How to take Matrix input from user:

R=int(input("Enter the number of rows:"))
C=int(input("Enter the number of columns:"))

# Intialize matrix
matrix=[]
print("Enter the entries row wise:")

# For user input
for i in range(R):                # A for loop for rows
    a=[]                        
    for j in range(C):            # A for loop for columns
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=' ')
    print()
