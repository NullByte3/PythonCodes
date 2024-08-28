vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

kuukausi = int(input("Anna kuukauden numero: "))

if kuukausi < 1 or kuukausi > 12:
    print("Ei ole kuukausi!")
else:
    vuodenaika = vuodenajat[kuukausi - 1]
    print(f"Kuukausi {kuukausi} kuuluu vuodenaikaan: {vuodenaika}")