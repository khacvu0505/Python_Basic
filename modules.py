# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
# Cách 1:
import datetime

today1 = datetime.date.today()

# Cách 2:
from datetime import date

today2 = date.today()

# YYYY-MM-DD HH:MM:ss
datetime_obj = datetime.datetime.now()

#
import time
# from time import time

timestamp = time.time()
print(timestamp)

# Pip modules
import camelcase

camel = camelcase.CamelCase()
text = 'hello three world'
print(camel.hump(text))

# Custom Modules
# import c1
import validator
# import c2
from validator import validate_email

email = 'khacvu0505@gmail.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Not an email')
