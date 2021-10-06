# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object


# Create Class
class User:
    # Constructor: chỗ này trong python dùng self thay vì this
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} an d I am {self.age}'

    def has_birthday(self):
        self.age += 1


# Init user object
vu = User('KhacVu', 'khacvu0505@gmail.com', 18)

# Edit property
vu.age = 22

vu.has_birthday()

# Call method
print(vu.greeting())


# Customer class
class Customer(User):
    def __init__(
        self,
        name,
        email,
        age,
    ):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(seft, balance):
        seft.balance = balance


#Init Customer
quyen = Customer('Hoang Quyen', 'hoangquyen8599@gmail.com', 20)
quyen.set_balance(400)
print(quyen.balance)
