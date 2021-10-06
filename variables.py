# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
# x=1  # Đây là chó
# y=2.5      #float
# name='Vu'    #string
# is_cool:True #boolean
# print(x)      

# Multipe Asssignment
x, y, name, is_cool=(1,2.5,'Vu',True)
print(x, y, name, is_cool)

#Basic math 
a=x+y
print(a)

# Check type(Kiểm tra kiểu dữ liệu)
# print(type(name))

#Casting(Ép kiểu)
x= str(x)
y= int(y)
z=float(y)

# Check type(Kiểm tra kiểu dữ liệu)
print(type(y))
print(z)