#korduv_tervitus.py

#toob programmi sisse ajamooduli
import time

def tervitus():

    if input("Kas tohib ma tervitan sind? (Y/n)") == "y":
    #peatab aja üheks sekundiks jätab mulje, et programm on interaktiivne
        time.sleep(1)
        print("Mitu korda ma teid tervitama pean?")
        #väljastab tervituse ekraanile
        for i in range(int(input())):
            print("Tervist")
    #siin analoogselt
    else:
        time.sleep(1)
        print("Selge, head päeva")

tervitus()