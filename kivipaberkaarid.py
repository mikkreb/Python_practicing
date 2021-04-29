# Rock paper scissors in Estonian
import random

draw = False
victory = None
opponent = ''
user = ''

while True:
    user = input("Kivi paber või käärid?: ")
    if user == 'kivi' or user == 'paber' or user == 'käärid':
        break

    if user == 'exit':
        exit()
    else:
        print("Programm sai vale sisendi!")
        print("Sisestage väikeste tähemärkidega kivi, paber või käärid")
        print("Kui soovite väljuda programmist kirjutage exit või vajutage CTRL+C")

def cpuresult():
    results = ['kivi','paber','käärid']
    result = results[random.randint(0, 2)]
    return result
def compare(o, u):
    result = None
    if o == 'käärid' and u == 'paber':
        result = False
    elif o == 'paber' and u == 'käärid':
        result = True
    elif o == 'kivi' and u == 'käärid':
        result = False
    elif o == 'käärid' and u == 'kivi':
        result = True
    elif o == 'paber' and u == 'kivi':
        result = False
    elif o == 'kivi' and u == 'paber':
        result = True
    return result

opponent = cpuresult()
print("Arvuti vastas: " + opponent)

if opponent == user:
    draw = True
elif draw != True:
    victory = compare(opponent, user)

if victory == True:
    print("Te võitsite!")
elif victory == False:
    print("Te kaotasite :(")

if draw == True:
    print("Te jäite viiki!")