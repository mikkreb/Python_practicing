#MATH GAME!!!
import random

answer = 0
mistakecounter = 0
wincounter = 0

print("WELCOME TO A FUN MATH GAME!!!\nAvailable gamemodes:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
gamemode = int(input("Please choose your gamemode 1/2/3/4: \n"))

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    x = random.randint(1, 100)
    y = random.randint(1, 100)

    if gamemode == 1:
        result = add(x, y)
        symbol = ' + '
    
    if gamemode == 2:
        result = subtract(x, y)
        symbol = ' - '
    
    if gamemode == 3:
        result = multiply(x, y)
        symbol = ' * '

    answer = int(input("\n What is " + x + symbol + y + "?")