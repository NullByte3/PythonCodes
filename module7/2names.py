nimet = set()

while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        break

    if nimi in nimet:
        print("Vanha nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print("Nimet ovat:")
for nimi in nimet:
    print(nimi)