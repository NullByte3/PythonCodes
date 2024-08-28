luku = int(input("Syötä luku: "))
on_alkuluku = True
for i in range(2, luku):
    if luku % i == 0:
        on_alkuluku = False
        break
if on_alkuluku:
    print(f"{luku} on alkuluku")
else:
    print(f"{luku} ei ole alkuluku")