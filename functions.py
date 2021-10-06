# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces


# Create function
def sayHello(name='Vũ'):
    '''
    Print hello and name.
    '''
    # print('Hello {name}'.format(name=name))
    print(f'Hello {name}')


sayHello("Quyên")

# Return value


def getSum(a=1, b=1):
    return a + b


print(getSum(1, 3))

# Add One To Num


def addOneToNum(num):
    return num + 1


print(addOneToNum(1))

# A lambda function is a small anonymous function.
# (lambda là 1 hàm nhỏ,ẩn danh)
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
# (lambda có thể nhận bất kỳ số lượng đối số nhưng chỉ có thể có một biểu thức)

getSum = lambda num1=2, num2=2: num1 + num2

print(getSum(5, 5))
