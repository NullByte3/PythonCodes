lentoasemat = {}

while True:
    print("Mitä haluat?")
    print("1: Uusi lentoasema")
    print("2: Hae lentoaseman tiedot")
    print("3: Lopeta?")

    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        icao = input("Lentoaseman ICAO-koodi: ")
        nimi = input("Lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print(f"Lentoasema {nimi} (ICAO: {icao}) lisätty.")

    elif valinta == "2":
        icao = input("Lentoaseman ICAO-koodi: ")
        if icao in lentoasemat:
            print(f"Lentoaseman nimi: {lentoasemat[icao]}")
        else:
            print("Lentoasemaa ei ole olemassa.")

    elif valinta == "3":
        print("Cya")
        break

    else:
        print("Yritä uudelleen.")