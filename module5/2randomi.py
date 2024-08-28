luvut = []
while True:
    luku = input("Syötä luku: ")
    if luku == "":
        break
    luvut.append(float(luku))
luvut.sort(reverse=True)
print("Viisi suurinta lukua ovat:")
for i in range(min(5, len(luvut))):
    print(luvut[i])