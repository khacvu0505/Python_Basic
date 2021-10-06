# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name='Vu'
age=18
#Concatnate
# print('Hello word. I am  ' +name + ' and I am '+ str(age) + ' yearsold' )

# String For matting

#Arguments by position(Lặp luận Theo vị trí)
# print('{},{},{}'.format('a','b','c'))
# print('{2},{0},{1}'.format('a','b','c'))


# Arguments by name 
# print('My name is {name} and I am {age}'.format(name='Vu',age=18))

# F-Strings(only 3.6+)
# print(f'My name is{name} and I am {age}')

# String Methods
s = 'hellO three world'

# Capitazile first letter(Viết hoa kí tự đầu tiên)
print(s.capitalize())

#Make all upper
print(s.upper())

#Make all lower
print(s.lower())

#Swap case
print(s.swapcase())

# Get Length 
print(len(s))

# Replace
print(s.replace('world','Vu la cho'))

# Count characters in strings
sub="h"
print(s.count(sub))

# Starts with 
'Hello tree world'
print(s.startswith('h')) # True

# End with 
'Hello tree world'
print(s.endswith('o'))  # False

# Split (Cut string)
print(s.split())

# Find position first
print(s.find('h'))

# Check is ALphanumber(Kiểm tra xem có phải là chữ với số hay không <=> Nghĩa là k được chứa ký tự đặc biệt) 
print('#####'.isalnum()) # False
print('khacvu05'.isalnum()) # True


# Check is alpha (Là chữ cái trong bảng chữ cái )
# print(s.isalpha()) # True
# print('a'.isalpha()) # True

# Check is numberic
print('3d'.isnumeric()) # False
print('3'.isnumeric()) # True