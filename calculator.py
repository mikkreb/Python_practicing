#a simple terminal based calculator made in Python
#currently handles addition, subtraction, multiplying and dividing

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide (x, y):
    return x / y

uinput = input("Add, subtract, multiply or divide?: ")
x = float(input("First float: "))
y = float(input("Second float: "))

if uinput == 'add':
    result = add(x, y)

if uinput == 'subtract':
    result = subtract(x, y)

if uinput == 'multiply':
    result = multiply(x, y)

if uinput == 'divide':
    result = divide(x, y)

print("\nThe answer is " + str(result))