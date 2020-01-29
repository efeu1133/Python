text = str(input("Eingabe: "))
string = {}

for i in text:
    if i in string:
        string[i] += 1
    else:
        string[i] = 1
print(string)
