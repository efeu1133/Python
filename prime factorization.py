# Initialisierung
primfaktoren = [[2, 2],[ 3, 7]]
# Verarbeitung
produkt = 1
for element in primfaktoren:
    print(element[0],element[1])
    produkt = produkt * element [0] * element[1]
# Ausgabe
print('Primfaktoren:', primfaktoren)
print('Zahl:', produkt)
