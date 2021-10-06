# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['Vu', 'Quyen', 'A', 'B', 'C']

# Simple for loop
# for person in people:
#     print(person)

# Breadk out
# for person in people:
#     if person == 'B':
#         break
#     print(person)

# Continue
# for person in people:
#     if person == 'Quyen':
#         continue
#     print(person)

# Range
# for i in range(len(people)):
#     print('Current people: ', people[i])

# for i in range(0, 10):
#     print(f'Number {i}')

# While loops execute a set of statements as long as a condition is true.

count = 0
while count <= 10:
    print(count)
    count += 1
