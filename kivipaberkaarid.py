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

opponent = cpuresult()
print("Arvuti vastas: " + opponent)

if opponent == user:
    draw = True
elif draw != True:
    if opponent == 'käärid' and user == 'paber':
        victory = False
    elif opponent == 'paber' and user == 'käärid':
        victory = True
    elif opponent == 'kivi' and user == 'käärid':
        victory = False
    elif opponent == 'käärid' and user == 'kivi':
        victory == True
    elif opponent == 'paber' and user == 'kivi':
        victory = False
    elif opponent == 'kivi' and user == 'paber':
        victory = True


if victory == True:
    print("Te võitsite!")
elif victory == False:
    print("Te kaotasite :(")

if draw == True:
    print("Te jäite viiki!")