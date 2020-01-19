kasten = []
Spalten = int(input("Spalten: "))
text = input("Text: ")
Zeilen = (len(text) // Spalten) + 1
for y in range (0,Spalten):
    zeile = []
    for x in range (0,Zeilen):
        zeile.append(" ")
    kasten.append(zeile)
#Prozess
i = 0
for y in range(0,Zeilen):
    for x in range(0,Spalten):
        kasten[x][y] = text[i]
        i = i+1
#Ende
for y in range(0,Zeilen):
    print(kasten[y])

