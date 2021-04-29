#tervitus.py

#toob programmi sisse ajamooduli
import time

#if-else tsükkel, küsib kasutajalt sisendit
#kõigepealt kirjutab programm välja "Kas tohib ma tervitan sind? "
#tühik on string andmetüübi järel, et vastus ekraanil normaalselt välja näeks
if input("Kas tohib ma tervitan sind? ") == "jah":
    #peatab aja üheks sekundiks jätab mulje, et programm on interaktiivne
    time.sleep(1)
    #väljastab tervituse ekraanile
    print("Tervist")
#siin analoogselt
else:
    time.sleep(1)
    print("Selge, head päeva")