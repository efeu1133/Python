import random
spielerstärke=int(input("Eingabe der Spielerstärke des Spielers B von 0-100: "))
ergebnis=[[0,0],[0,0],[0,0],[0,0],[0,0]]
x=0
gA=0
gB=0
while (x<=4):
    z1=random.randint(11,100)
    print("Zufallszahl",(z1))
    z2=z1-2
    z3=random.randint(0,1)
    print("z3",z3)
    if z3==0:
        z3=(z3+(spielerstärke/100))
        print ("z3",z3)
        z3=round(z3+0.01)
    print("z3 gerundet",z3)
    print ("spielerstärke durch 100",spielerstärke/100)
    if z3==0:
        z4=z1
        z5=z2
    else:
        z4=z2
        z5=z1
    if (z4+z5>=11) and ((z4>=11) or (z5>=11)):
       ergebnis[x][0]=z4
       ergebnis[x][1]=z5
    if (z4>z5):
        gA+=1
        print("Gewinner A",gA)
    else:
        gB+=1
        print("Gewinner B",gB)
    if (gA>2) or (gB>2):
        x=x+100
        print("x-nach-exit",x)
    x=x+1
    print("x",x)
    print("-------------")
print(ergebnis)
if gB>gA:
    print("Der Gewinner ist Spieler B")
else:
    print("Der Gewinner ist Spieler A")









#####(z1+z2>=11) and ((z1>=11) or (z2>=11)) and (x<=4)
#A1=int(input("Ergebnis Spieler A Satz 1: "))
#ergebnis[0][0]=A1
#B1=int(input("Ergebnis Spieler B Satz 1: "))
#ergebnis[0][1]=B1
#A2=int(input("Ergebnis Spieler A Satz 2: "))
#ergebnis[1][0]=A2
#B2=int(input("Ergebnis Spieler B Satz 2: "))
#ergebnis[1][1]=B2
#A3=int(input("Ergebnis Spieler A Satz 3: "))
#ergebnis[2][0]=A3
#B3=int(input("Ergebnis Spieler B Satz 3: "))
#ergebnis[2][1]=B3
#A4=int(input("Ergebnis Spieler A Satz 4: "))
#ergebnis[3][0]=A4
#B4=int(input("Ergebnis Spieler B Satz 4: "))
#ergebnis[3][1]=B4
#A5=int(input("Ergebnis Spieler A Satz 5: "))
#ergebnis[4][0]=A5
#B5=int(input("Ergebnis Spieler B Satz 5: "))
#ergebnis[4][1]=B5
