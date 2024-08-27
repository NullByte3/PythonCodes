oikea_tunnus = "python"
oikea_salasana = "rules"
yritykset = 0
while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    else:
        print("Väärä tunnus tai salasana")
        yritykset = yritykset + 1
if yritykset == 5:
    print("Et ole oikea käyttäjä!!!!!")