# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
userJSON = '{"first_name":"Vu", "last_name":"Nguyen","age":30}'

# Parse to dict
# json.loads(): giúp parse từ json string to dictionary
user = json.loads(userJSON)
print(user)
print(user['age'])

# dicitionary to JSON
# json.dumps(): help convert Json Object to Json String
car = {'make': 'Ford', 'model': 'Mustang', 'year': 2021}
carJSON = json.dumps(car)
print(carJSON)
