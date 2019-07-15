# Tuple
# It is immutable(non-changeable). We cannot add, remove or change an item in tuple.

# Creating a tuple
games=('Badminton','Cricket','Football')
print(games)

# Accessing tuple items
print(games[1])
print(games[-1])

# To get all the items of tuple
for x in games:
    print(x)
    print(id(x))  # Tuple doesn't allocate continuous memory to it's items

# Length of tuple
print(len(games))

# count() return the number of times the given value occurs in tuple
print(games.count('Badminton'))
