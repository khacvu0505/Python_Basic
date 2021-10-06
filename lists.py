# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create List
# numbers=[1,2,3,4,5]

# Using a constructor
numbers=list((1,2,3,4,5))
fruits=['Apple','Oranges','Grapes','Pears']

# Get Value
print(fruits[1])

# Get Length List
print(len(fruits))

# Append To List 
fruits.append('Banana')

# Remove from fruits
fruits.remove('Grapes')

# Insert into position(Thêm vào vị trí chỉ định)
fruits.insert(2,'Vũ')

# Remove from position(Xóa từ vị trí chỉ định)
fruits.pop(0)

# Reverse arr fruit
fruits.reverse()

# Sort 
fruits.sort()

# Reverse Sort
fruits.sort(reverse=True)

print(fruits)