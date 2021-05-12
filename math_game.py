#MATH GAME!!!
import random

answer = 0
win = 0
lose = 0

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
    elif gamemode == 2:
        result = subtract(x, y)
        symbol = ' - '
    elif gamemode == 3:
        result = multiply(x, y)
        symbol = ' * '
    
    answer == int(input("What is " + str(x) + str(symbol) + str(y) + ":"))

    if answer == result:
        print("Correct!")
        win += 1
    elif answer != result:
        print("Wrong!")
        lose +=1
    
    if lose >= 3:
        print("You lost!")
        break
    elif win >= 10:
        print("You answered 10 problems correctly!")
        break
