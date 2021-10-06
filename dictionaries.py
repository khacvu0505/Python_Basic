# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# (Là 1 bộ sưu tập có thể thay đổi và lập chỉ mục mà k có item(thành viên) trùng lặp)

# Simple dict
person={
  'first_name':'Nguyen',
  'last_name':'Vu',
  'age':18
}

# Using a constructor
# person= dict(first_name='Hoang',last_name='Quyen',age=18)

# Access value(Lấy ra một thuộc tính của đối tượng)
print(person['first_name']) #C1
print(person.get('last_name')) #C2: ngoài ra cũng có thể sử dụng method get

# Add key/value
person['phone']='555-555-555'

# Get key in dict (obj)
print(person.keys())

# Get value
print(person.values())

# Get item
print(person.items()) # dict_items([('first_name', 'Nguyen'), ('last_name', 'Vu'), ('age', 18), ('phone', '555-555-555')])

# Make copy
person2=person.copy()
person2['city']='Phan Rang'
print(person2)

# Remove item
del (person['age']) #C1
person.pop('phone') #C2


# Clear dict
person.clear()

# Get length
print(len(person2))

# List of dict 
people=[
  {'name':'Vu','age':18},
  {'name':'Quyen','age':18},
]
print(people[1]['name'])