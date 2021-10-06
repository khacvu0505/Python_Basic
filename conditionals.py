# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 5

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
# if x == y:
#   print(f'{x} is equal to {y}')

# If/else
# if x > y:
#   print(f'{x} is greater to {y}')
# else:
#   print(f'{x} is less to {y}'

# elif
if x > y:
    print(f'{x} is greater to {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{x} is less to {y}')

# Nested if
if x > 2:
    if x < 8:
        print('X >2 and <8')

# Logical operators (and, or, not) - Used to combine conditional statements

# And
# if (x > 2 and x < 10):
#     print('X lon hon 2 va nho hon 10')

# Or
# if (x > 2 or x < 10):
#     print('X lon hon 2 hoac nho hon 10')

# Not
# if not (x == y):
#     print(f'{x} is not equal to {y}')

# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1, 2, 3, 4, 5]
# in
# if (x in numbers):
#     print(x in numbers)

# not in
# if (x not in numbers):
#     print(x not in numbers)

# is
# if (x is y):
#   print(x is y)

# is not
# if (x is not y):
#     print(x is not y)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
