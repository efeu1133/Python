diagonal = 2
zeilen = 3
spalten = 3
#Yang-Hui-Quadrat

#summediagonal
#summezeilen
#summespalten

#x = x*x
#zahlen = 9
#summeallgemein = 15
#n>2 ist notwendig

#summediagonal
#summezeilen
#summespalten

feld1 = int(input("Eingabe des 1. Feldes: "))
feld2 = int(input("Eingabe des 2. Feldes: "))
feld3 = int(input("Eingabe des 3. Feldes: "))

feld4 = int(input("Eingabe des 4. Feldes: "))
feld5 = int(input("Eingabe des 5. Feldes, beachte dass dies 5 sein muss: "))
feld6 = int(input("Eingabe des 6. Feldes: "))

feld7 = int(input("Eingabe des 7. Feldes: "))
feld8 = int(input("Eingabe des 8. Feldes: "))
feld9 = int(input("Eingabe des 9. Feldes: "))

#summediagonal1:
#feld1
#feld5
#feld9

#summediagonal2
#feld3
#feld5
#feld7

#summezeilen:
#feld1
#feld4
#feld7

#summespalten1:
#feld1
#feld2
#feld3

#summespalten2:
#feld4
#feld5
#feld6

#summespalten3:
#feld7
#feld8
#feld9


def magischesQuadrat():
    while zeilen and spalten and diagonal==True:
        n=int(input("Eingabe einer natürlichen Zahl: "))
        if n>2:
            summeallgemein == 34
            zahlen ==16
        elif feld5==5:
            summespalten1 = feld1 + feld2 + feld3
            summespalten2 = feld4 + feld5+ feld6
            summespalten3 = feld7 + feld8 + feld9
        elif feld5==5:
            summezeilen = feld1 + feld4 + feld7
        elif feld5==5:
            summediagonal1 = feld1 + feld5 + feld9
        elif feld5==5:
            summediagonal2 = feld3 + feld5 + feld7
        else:
            print("Nicht möglich!")
    return summezeilen
    return summediagonal1
print(magischesQuadrat(summediagonal1))
