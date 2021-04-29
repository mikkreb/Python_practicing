# Rock paper scissors in Estonian
import random

print("Vastake väikeste tähemärkidega!")

draw = False
victory = None
opponent = ""
user = input("Kivi paber või käärid? ")

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
        result == True
    elif o == 'paber' and u == 'kivi':
        result = False
    elif o == 'kivi' and u == 'paber':
        result = True
    else:
        print("Arvuti ei saanud sobivat sisendit!")
        print("Palun sisestage kivi, paber või käärid!")
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