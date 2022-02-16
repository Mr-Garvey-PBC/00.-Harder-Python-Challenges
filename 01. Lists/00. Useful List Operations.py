aList=[]  # An empty list called aList]

bList=[56,78,100,45,88]  # A list containing integers
# Each list is made up of elements, starting at index position 0

# Operations to modify a list
# 1. Add an item to a list.  (Append)
aList.append(100)
aList.append(20)
aList.append(99)
print(aList)

# 2. Remove an item to a list.
aList.remove(99)
print(aList)

# 3. Length of a list
x=len(bList)
print(x)

# 4. Index of a list element (location)
print(bList.index(100))

# 5. Insert an item into specific index place
bList.insert(0,22)
print(bList)

# 6. Calling different elements of a list
print(bList[1])

for index_position in range (len(bList)):
    print(bList[index_position])


 